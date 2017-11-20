import requests

class DataApiClient(object):
    """http data api client"""
    # http://dataapi20171117020514.azurewebsites.net/api/data
    apiURL = 'http://localhost:2500/api/Data'

    def __init__ (self):

    get():
        r = requests.get(apiURL)
        return r.Content
    is_changed():
        return True



    
