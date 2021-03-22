"""Script to translate single address to coordinates that marks the result on a map for validation"""
import geopy
from geopy.geocoders import Nominatim
import folium

def convertPlaceToCoord(p):
    """Converts an address given as string into longitude and latitude coordinates and adds the location to map"""
    map = folium.Map(location=[51.94986285,7.60407079384229],
                            zoom_start=12,
                            tiles='cartodbpositron')

    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(p)
    lat = location.latitude
    lon = location.longitude

    if (lat != None and lon != None):
        folium.Marker([lat, lon], popup=p).add_to(map)
    map.save("singleCoord.html")
