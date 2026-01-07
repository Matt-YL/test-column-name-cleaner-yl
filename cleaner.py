def clean_column_name(name: str) -> str:
    """
    Standardize column names for ETL usage.
    """
    return (
        name.strip()
        .lower()
        .replace(" ", "_")
    )
