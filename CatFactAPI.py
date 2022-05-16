import requests

class CatFactAPI:
  CATAPIURL = "http://meowfacts.herokuapp.com/"

  def __init__(self):
    pass
    
  def get(self):
      return (requests.get("http://meowfacts.herokuapp.com/").text)
      #creates return statement sending random cat fact to caller
  