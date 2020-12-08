# covid_geo

Covid19 Geo Map 🗺 📍

## Getting Started

COVID19 Geo & Heat Map using covid19api.com

### Prerequisites

- Python
- Pandas *Data Normalization*
- Folium *Geo Data*

```
# Normalize data
pd.json_normalize(covid1['Countries'], sep=",")
```

```
# Generate base map
map = folium.Map(tiles="Stamen Terrain", min_zoom=1.5)
```

## Built With

* [COVID19API](https://covid19api.com//) - API
* [Folium](https://raw.githubusercontent.com/python-visualization/folium/master/examples/data) - Geo Data
