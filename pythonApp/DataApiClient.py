import requests

class DataApiClient(object):
    """http data the api client"""
    apiURL = ""
    def __init__ (self):
    # http://dataapi20171117020514.azurewebsites.net/api/data
    self.apiURL = "http://localhost:2500/api/Data"

    get():
        r = requests.get(self.apiURL)
        return r.Content
    is_changed():
        return True
