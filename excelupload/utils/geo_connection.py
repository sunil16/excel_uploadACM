
from geopy.geocoders import Nominatim


def get_geo_conn():
    try:
        geolocator = Nominatim()
    except Exception as e:
        print("Error in Maps Client file:geo_connection", e)
    return geolocator
