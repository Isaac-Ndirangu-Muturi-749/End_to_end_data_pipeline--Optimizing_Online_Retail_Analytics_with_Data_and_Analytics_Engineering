from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


import pyarrow as pa
import pyarrow.parquet as pq
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/direct-disk-412820-2333e42872f1.json'

bucket_name = 'mage_data_engineering_zoomcamp'
project_id = 'direct-disk-412820'

table_name = "e_commerce_data"
# Define the path to the root directory containing the partitioned Parquet files in GCS
gcs_root_path = f'gs://{bucket_name}/{table_name}'


@data_loader
def load_from_google_cloud_storage(*args, **kwargs):

    # Create a ParquetDataset instance pointing to the root path in GCS
    dataset = pq.ParquetDataset(
        gcs_root_path
        )
    # Read the dataset into a Pandas DataFrame
    df = dataset.read().to_pandas()
    return df
