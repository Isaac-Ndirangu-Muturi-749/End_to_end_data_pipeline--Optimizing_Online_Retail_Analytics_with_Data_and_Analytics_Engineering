from deltalake import DeltaTable
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_table(*args, **kwargs):
    """
    Load a Delta Table

    Docs: https://delta-io.github.io/delta-rs/python/usage.html#loading-a-delta-table
    """
    storage_options = {
        'GOOGLE_SERVICE_ACCOUNT': '',
        'GOOGLE_SERVICE_ACCOUNT_PATH': '',
        'GOOGLE_SERVICE_ACCOUNT_KEY': '',
        'GOOGLE_BUCKET': '',
    }

    uri = 'gs://[bucket]/[key]'

    dt = DeltaTable(uri, storage_options=storage_options)

    return dt.to_pandas()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'