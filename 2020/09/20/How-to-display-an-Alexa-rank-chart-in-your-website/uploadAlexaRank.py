# Upload the JSON file to my Azure Blob Storage
from azure.storage.blob import BlockBlobService
print "Beginning to upload the JSON file"
blob_service = BlockBlobService(config['accountName'], config['accountKey'])
full_path_to_file = config['excelFilePath'] +\
  full_file_name
blob_service.create_blob_from_path(
  config['containerName'],
  full_file_name,
  full_path_to_file)
print "Finished uploading the JSON file"