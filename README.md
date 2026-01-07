# Column Name Cleaner

A simple Python utility to standardize column names for ETL and data analysis.

## What it does
- Lowercases column names
- Replaces spaces with underscores
- Removes leading/trailing spaces

## Example
```python
from cleaner import clean_column_name

clean_column_name(" Order Date ")
# output: order_date
