import json
import requests
import mimetypes
import http.client
import pandas as pd
import folium
from folium.plugis import HeatMap
from pandas.io.json import json_normalize


conn = http.client.HTTPSConnection("api.covid19api.com")
payload = ''
headers = {}
conn.request("GET", "/summary", payload, headers)
re = conn.getresponce()
data = res.read().decode("UTF-8")
