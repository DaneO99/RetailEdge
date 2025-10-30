from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_connection():
    """Create a SQLAlchemy engine for the superstore MySQL database."""
    try:
        db_host = os.getenv('DB_HOST')
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        
        # Create connection string
        connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
        
        # Create engine
        engine = create_engine(connection_string)
        
        # Test connection
        with engine.connect() as conn:
            print("Successfully connected to superstore database")
        
        return engine
    except Exception as e:
        print(f"Error: {e}")
        return None

def close_connection(engine):
    """Close the database connection."""
    if engine:
        engine.dispose()
        print("Connection closed")

# Example usage
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        close_connection(conn)
