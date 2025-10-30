from src.db_connection import create_connection, close_connection
import pandas as pd

# Connect to database
conn = create_connection()

# Query data
query = "SELECT * FROM sales LIMIT 200"
df = pd.read_sql(query, conn)

# View data
print(df)

# Close connection
close_connection(conn)
