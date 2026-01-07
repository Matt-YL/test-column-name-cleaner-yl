# test_extra.py
from cleaner import clean_column_name_full

def test_hyphen():
    assert clean_column_name_full("Order-Date") == "order_date"