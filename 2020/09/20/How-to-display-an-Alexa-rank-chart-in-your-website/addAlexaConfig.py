import os
config = {}

# config for your site
config["website"] = "https://poanchen.github.io"

# config for your ifttt
config["iftttApiEndpoint"] = "https://maker.ifttt.com/trigger/%s/with/key/%s"
config["iftttEventName"] = "add_alexa_rank"
config["iftttApiMakerKey"] = os.environ['IFTTTAPIMAKERKEY'] # get the key from https://ifttt.com/maker_webhooks/settings

# config for alexa site
config["alexaCli"] = 10
config["alexaApiEndpoint"] = "http://data.alexa.com/data"