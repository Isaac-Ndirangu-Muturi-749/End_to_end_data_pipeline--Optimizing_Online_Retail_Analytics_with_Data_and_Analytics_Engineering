if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    # Perform data transformations
    data = parse_dates(data)
    data = rename_columns(data)
    data = clean_description(data)
    data = calculate_total_price(data)
    data = drop_duplicates(data)
    data = fill_missing_values(data)
    data = preprocess_datetime(data)
    data = filter_debt_rows(data)
    data = filter_cancelled_purchases(data)
    return data

def parse_dates(data):
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%m/%d/%Y %H:%M')
    return data

def rename_columns(data):
    data.rename(columns={
        'InvoiceNo': 'invoice_no',
        'StockCode': 'stock_code',
        'Description': 'description',
        'Quantity': 'quantity',
        'UnitPrice': 'unit_price',
        'CustomerID': 'customer_id',
        'Country': 'country',
        'InvoiceDate': 'invoice_datetime'
    }, inplace=True)
    return data

def clean_description(data):
    data['description'] = data['description'].str.lower()
    return data


def calculate_total_price(data):
    data['total_price'] = data['quantity'] * data['unit_price']
    return data

def drop_duplicates(data):
    data = data.drop_duplicates()
    return data

def fill_missing_values(data):
    data['description'] = data['description'].fillna("Unknown")
    data['customer_id'] = data['customer_id'].fillna(0)
    return data

def preprocess_datetime(data):
    data['time'] = data['invoice_datetime'].dt.time
    data['month'] = data['invoice_datetime'].dt.month_name()
    data['day'] = data['invoice_datetime'].dt.day_name()
    data['year'] = data['invoice_datetime'].dt.year
    return data

def filter_debt_rows(data):
    mask = data['description'].str.contains('debt', case=False)
    data = data[~mask]
    return data

def filter_cancelled_purchases(data):
    cancelled_purchases = data[data['quantity'] < 0]
    data = data[data['quantity'] > 0]
    return data
