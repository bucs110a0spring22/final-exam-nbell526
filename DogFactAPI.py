import requests

class DogFactAPI:
  DOGAPIURL = "http://dog-api.kinduff.com/api/facts"

  def __init__(self):
    pass
    
  def get(self):
    return (requests.get("http://dog-api.kinduff.com/api/facts").text)
      #creates return statement sending random dog fact to caller