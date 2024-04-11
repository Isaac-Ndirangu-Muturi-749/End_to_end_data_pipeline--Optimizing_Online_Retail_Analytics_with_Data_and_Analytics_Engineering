from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def l(data, *args, **kwargs):

    return data.head()


