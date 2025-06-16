import requests
from math import radians, cos, sin, asin, sqrt
def geocode_address_osm(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "ifri-covoiturage-app"
    }
    resp = requests.get(url, params=params, headers=headers).json()
    if resp:
        return float(resp[0]['lat']), float(resp[0]['lon'])
    return None, None

def haversine(lat1, lon1, lat2, lon2):
   
    R = 6371  # Rayon de la Terre en km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return R * c * 1000  # distance en mètres