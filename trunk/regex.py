from urllib2 import urlopen, Request
import json
from pprint import pprint

def getreq(url):
  u = urlopen(url)
  resp = json.loads(u.read().decode('utf-8'))
  print "Hello, Welcome to Weather forecasts"
  pprint(resp)

if __name__=="__main__":
  url = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=396d713c5b99c4d28dbb68d36ea54d1e"
  getreq(url)
