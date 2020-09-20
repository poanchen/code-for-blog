import requests, csv, re
execfile("config.py")

# Download the sheets
print "Beginning to download the CSV from Google Sheets"
r = requests.get(config['excelDownloadUrl'])
open(config['excelFileName'], 'wb').write(r.content)
print "Finished downloading the sheets..."