import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    df_dtypes = {
                    'InvoiceNo':str,
                    'StockCode':str,
                    'Description':str,
                    'Quantity':pd.Int64Dtype(),
                    'UnitPrice':float,
                    'CustomerID':str,
                    'Country':str
    }


    url = 'https://github.com/Isaac-Ndirangu-Muturi-749/capstone_de_zoom/raw/main/data/Online%20Retail.xlsx'

    df = pd.read_excel(url, dtype=df_dtypes)

    return df