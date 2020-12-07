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


# Normalize data
pd.json_normalize(covid1['Countries'], sep=",")

# Convert to Pandas data frame
df = pd.DataFrame(covid1['Countries'])
# df

# Drop column we don't need
covid2 = df.drop(columns=['CountryCode', 'Slug', 'Date', 'Premium'], axis=1)
# covid2

# Generate base map
map = folium.Map(tiles="Stamen Terrain", min_zoom=1.5)
# map


# gets geodata
url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"

country_shapes = f'{url}/world-countries.json'

# Generate choropleh map layer
folium.Choropleth(
    geo_data=country_shapes,
    min_zoom=2,
    name='Covid-19',
    data=covid2,
    columns=['Country', 'TotalConfirmed'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    nan_fill_color='black',
    legend_name='Total Confirmed Covid Cases',
).add_to(map)

# Generate circular makers
covid2.update(covid2['TotalConfirmed'].map('Total Confirmed:{}'.format))
covid2.update(covid2['TotalRecovered'].map('Total Recovered:{}'.format))

coordinates = pd.read_csv(
    'https://raw.githubusercontent.com/VinitaSilaparasetty/covid-map/master/country-coordinates-world.csv')


# coordinates
covid_final = pd.merge(covid2, coordinates, on='Country')

# Plotting


def plotDot(point):
    folium.CircleMarker(location=[point.latitude, point.longitude],
                        radius=5,
                        weight=2,
                        popup=[point.Country, point.TotalConfirmed,
                               point.TotalRecovered],
                        fill_color='#000000'
                        ).add_to(map)


covid_final.apply(plotDot, axis=1)
map.fit_bounds(map.get_bounds())
# map

# Generate base map
m1 = folium.Map(tiles='StamenToner', min_zoom=2)
# m1


deaths = covid_final['TotalDeaths'].astype(float)
lat = covid_final['latitude'].astype(float)
lon = covid_final['longitude'].astype(float)

# Heat map
m1.add_child(HeatMap(zip(lat, lon, deaths), radius=0))
