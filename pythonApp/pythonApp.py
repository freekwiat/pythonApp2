import requests
from Clipboard import Clipboard

# http://dataapi20171117020514.azurewebsites.net/api/data

websiteURL = 'http://localhost:2500/api/Data'

r = requests.get(websiteURL)

clipboard =  Clipboard()

clipboard.get()
clipboard.add()
print (r.text)
print (r.content)