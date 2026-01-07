def clean_column_name(name: str) -> str:
    """
    Standardize column names for ETL usage.
    """
    return (
        name.strip()
        .lower()
        .replace(" ", "_")
    )

def clean_column_name_full(name: str) -> str:
    return name.strip().lower().replace(" ", "_").replace("-", "_")
