# SQL

This folder contains SQL query files for database analysis and exploration.

## Purpose

This directory stores raw SQL scripts that can be:
- Executed in DBeaver or other database clients
- Referenced by Python scripts
- Used for ad-hoc analysis and reporting
- Shared and version-controlled for reproducibility

## Database

**Database Name**: `superstore`  
**Table**: `sales`

Connection details are stored in the `.env` file (not tracked in git).

## File Organization

SQL files are typically organized by purpose:
- Exploratory queries
- Aggregations and summaries
- Data quality checks
- Report generation queries

## Running Queries

### In DBeaver:
1. Open the SQL file
2. Make sure the `superstore` database is selected
3. Execute the query

### In Python:
```python
from src.db_connection import create_connection, close_connection
import pandas as pd

engine = create_connection()

# Read SQL file
with open('SQL/query_file.sql', 'r') as f:
    query = f.read()

df = pd.read_sql(query, engine)
close_connection(engine)
```

## Best Practices

- Use descriptive file names (e.g., `sales_by_region.sql`, `top_customers.sql`)
- Add comments in SQL files to explain complex queries
- Format SQL for readability
- Keep queries modular and reusable
