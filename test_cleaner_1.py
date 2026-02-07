from cleaner import clean_column_name

def test_basic():
    assert clean_column_name(" Order Date ") == "order_date"
