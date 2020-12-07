import json
import requests
import mimetypes
import http.client
import pandas as pd
import folium
from folium.plugis import HeatMap
from pandas.io.json import json_normalize

# Data Request
conn = http.client.HTTPSConnection("api.covid19api.com")
payload = ''
headers = {}
conn.request("GET", "/summary", payload, headers)
res = conn.getresponse()
data = res.read().decode("UTF-8")

# Convert Data to JSON
covid1 = json.loads(data)
