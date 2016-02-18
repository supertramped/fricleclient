import urllib2
import urllib
import json
import copy

class Client:
    FRICLE_URL = "http://fricles.com:8080/fricles/api/v1/get_sentiments"
    INPUT_TPL = { "inputs" : {"api_key" :  "46:3a:bf:30:42:03:5d:83:e1:21:28:32:f6:f0:38:39",  "text" :""} }
    def __init__(self, api_key=""):
        self.api_key = api_key

    def run(self, text):
        inputData = copy.deepcopy(self.INPUT_TPL.copy())
        inputData["inputs"]["text"] = text
        inputData["inputs"]["api_key"] = self.api_key
        params = urllib.urlencode(inputData)
        request = urllib2.Request(self.FRICLE_URL, data=inputData, headers={ 'Content-Type':'application/json' })
        try:
            response = urllib2.urlopen(request).read()
            return json.loads(response)
        except urllib2.HTTPError, err:
            return {"status": "FAILED","http_code" : err.code, "message" : err.message}
        except urllib2.URLError, err:
            return {"status": "FAILED","http_code" : err.errno, "message" : err.reason}
        except Exception as excep:
            return {"status" : "ERROR", "http_code": -1, "message": excep.message}
