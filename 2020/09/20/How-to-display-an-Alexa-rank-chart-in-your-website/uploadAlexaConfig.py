import os
config = {}

config['excelDownloadUrl'] = "urlToYourGoogleSheet" # for example, "https://docs.google.com/spreadsheets/d/XXXXXXXXXXXXX/export?format=csv"
config['excelFileName'] = "poanchen - alexa"
config['excelFileExtension'] = "json"
config['excelFilePath'] = "./"

# Azure Portal
config['accountName'] = "poanchengithubio"
config['accountKey'] = os.environ['AZUREPORTALACCOUNTKEY'] # get the key from https://portal.azure.com

# Azure Blob Storage
config['containerName'] = "poanchen"
