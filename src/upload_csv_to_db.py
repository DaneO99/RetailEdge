import pandas as pd
import sys
import os
from db_connection import create_connection, close_connection

def upload_csv_to_database(csv_path, table_name='sales'):
    """Upload CSV data to MySQL database."""
    
    # Read CSV file
    print(f"Reading CSV file: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows")
    
    # Clean column names (replace spaces with underscores, lowercase)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Connect to database
    connection = create_connection()
    if not connection:
        print("Failed to connect to database")
        return
    
    try:
        cursor = connection.cursor()
        
        # Create table if it doesn't exist
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            row_id INT PRIMARY KEY,
            order_id VARCHAR(50),
            order_date DATE,
            ship_date DATE,
            ship_mode VARCHAR(50),
            customer_id VARCHAR(50),
            customer_name VARCHAR(100),
            segment VARCHAR(50),
            country VARCHAR(100),
            city VARCHAR(100),
            state VARCHAR(50),
            postal_code VARCHAR(20),
            region VARCHAR(50),
            product_id VARCHAR(50),
            category VARCHAR(50),
            sub_category VARCHAR(50),
            product_name VARCHAR(255),
            sales DECIMAL(10,2),
            quantity INT,
            discount DECIMAL(5,2),
            profit DECIMAL(10,4)
        )
        """
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' ready")
        
        # Convert date columns to proper format
        df['order_date'] = pd.to_datetime(df['order_date']).dt.strftime('%Y-%m-%d')
        df['ship_date'] = pd.to_datetime(df['ship_date']).dt.strftime('%Y-%m-%d')
        
        # Insert data
        insert_query = f"""
        INSERT INTO {table_name} 
        (row_id, order_id, order_date, ship_date, ship_mode, customer_id, 
         customer_name, segment, country, city, state, postal_code, region, 
         product_id, category, sub_category, product_name, sales, quantity, 
         discount, profit)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s)
        """
        
        # Insert rows
        for index, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))
            if (index + 1) % 100 == 0:
                print(f"Inserted {index + 1} rows...")
        
        connection.commit()
        print(f"Successfully uploaded {len(df)} rows to '{table_name}' table")
        
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        close_connection(connection)

if __name__ == "__main__":
    # Path to CSV file
    csv_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Data', 'superstore.csv')
    upload_csv_to_database(csv_file)
