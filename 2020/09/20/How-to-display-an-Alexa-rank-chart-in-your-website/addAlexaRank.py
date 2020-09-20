import requests, xml.etree.ElementTree as ET, sys
execfile("config.py")
CLI = config["alexaCli"]

def getDefaultAlexaParams(url, cli=CLI):
  return """?cli=%d&url=%s""" % (cli, url)
def getDefaultAlexaPostParams(gr, cn, cr):
  return {"value1": gr, "value2": cn, "value3": cr}
def getGlobalRankIfAny(xml):
  try:
    return xml[0].find("POPULARITY").get("TEXT")
  except:
    pass
def getCountryNameIfAny(xml):
  try:
    return xml[0].find("COUNTRY").get("NAME")
  except:
    pass
def getCountryRankIfAny(xml):
  try:
    return xml[0].find("COUNTRY").get("RANK")
  except:
    pass

if __name__ == "__main__":
  # getting site rank from Alexa api
  r = requests.get(config["alexaApiEndpoint"] + 
    getDefaultAlexaParams(config["website"]))
  if r.status_code != requests.codes.ok:
    print "Alexa api end-point went wrong. Please try again later"
    sys.exit(0)

  # reading the xml and retrieve the rank
  xml = ET.fromstring(r.content)

  # trigger the ifttt api
  payload = getDefaultAlexaPostParams(getGlobalRankIfAny(xml),
    getCountryNameIfAny(xml),
    getCountryRankIfAny(xml))
  r = requests.post(config["iftttApiEndpoint"] % \
    (config["iftttEventName"], config["iftttApiMakerKey"]), 
    data=payload)
  if r.status_code != requests.codes.ok:
    print "Ifttt api end-point went wrong. Please try again later"
    sys.exit(0)
  print "yaa, entry has been added to your Google spreadsheet"
