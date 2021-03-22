"""The script converts all addresses from the Ort table into coordinates using the geopy library. The results are marked on a map for validation"""

import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import folium
from folium.plugins import FastMarkerCluster
from folium.plugins import MarkerCluster
from folium.plugins import Draw
from geopy.extra.rate_limiter import RateLimiter
import json
import mysql.connector


#Connects to the database.
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="geschichtswettbewerb",
    auth_plugin='caching_sha2_password'
)

mycursor = db.cursor()

locator = Nominatim(user_agent="myGeocoder")

#Convert all addresses to coordinates

df = pd.read_csv("path/to/Ort.csv", sep=",")

df['ADDRESS'] = df['Ortbezeichnung'].astype(str)

geocode = RateLimiter(locator.geocode, min_delay_seconds=1, error_wait_seconds=10)
df['location'] = df['ADDRESS'].apply(geocode)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
df = df.drop(['location', 'lat', 'lon', 'altitude', 'point'], axis=1)
df.to_csv(r'Ort.csv', index = False)

df = pd.read_csv("/Users/richardalbrecht/Desktop/BA/geschichtswettbewerb/Ort.csv", sep=",")

df = df[pd.notnull(df["latitude"])]

#create new map
folium_map = folium.Map(location=[51.94986285,7.60407079384229],
                        zoom_start=12,
                        tiles='cartodbpositron')#CartoDB dark_matter

#create a marker cluster
marker_cluster = MarkerCluster().add_to(folium_map)

#Get coordinates from database
la = []
lo = []
ortBez = []
def getCoords():
    """Function to get the coordinates from the database"""
    Q = 'SELECT o.lon, o.lat, o.Ortbezeichnung from karte_ort o'
    mycursor.execute(Q)
    for x in mycursor:
        print(x[0])
        lo.append(x[0])
        print(x[1])
        la.append(x[1])
        print(x[2])
        ortBez.append(x[2])

getCoords()

#add markers to map
for i in range(0, len(la)):
    if la[i] != None:
        folium.Marker([lo[i], la[i]], popup=ortBez[i]).add_to(marker_cluster)

#Adds a layer control to the map
folium.LayerControl().add_to(folium_map)

folium_map.save("map.html")
