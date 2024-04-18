if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


import pyarrow as pa
import pyarrow.parquet as pq
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/direct-disk-412820-2333e42872f1.json'

bucket_name = 'mage_data_engineering_zoomcamp'
project_id = 'direct-disk-412820'

table_name = "online_retail_data"
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    data['invoice_date'] = data['invoice_datetime'].dt.date

    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['invoice_date'],
        filesystem=gcs
    )