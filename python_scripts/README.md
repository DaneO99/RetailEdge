# Python Scripts

This folder contains Python scripts for querying and analyzing the superstore database.

## Purpose

Scripts in this folder are used to:
- Execute SQL queries via Python
- Perform data analysis using Pandas
- Generate reports and export results
- Create data transformations and aggregations

## Running Scripts

All scripts should be run from the **project root directory** using the module syntax:

```bash
python3 -m python_scripts.script_name
```

For example:
```bash
python3 -m python_scripts.view_first_200
```

## Script Structure

Each script typically follows this pattern:

```python
from src.db_connection import create_connection, close_connection
import pandas as pd

# Connect to database
engine = create_connection()

# Your SQL query
query = "SELECT * FROM sales LIMIT 200"
df = pd.read_sql(query, engine)

# Your analysis code here
print(df)

# Close connection
close_connection(engine)
```

## Dependencies

- SQLAlchemy (for database connections)
- Pandas (for data manipulation)
- python-dotenv (for environment variables)

Database credentials are stored in `.env` file (not tracked in git).

## Adding New Scripts

When creating new analysis scripts:
1. Place them in this `python_scripts/` folder
2. Import database connection from `src.db_connection`
3. Run from project root using `-m python_scripts.script_name`
