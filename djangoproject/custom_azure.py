from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'Your Secret Key Here' # Must be replaced by your <storage_account_name>
    account_key = 'Your Secret Key Here' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'Your Secret Key Here' # Must be replaced by your storage_account_name
    account_key = 'Your Secret Key Here' # Must be replaced by your <storage_account_key>
    azure_container = 'mypublic-container'
    expiration_secs = None


