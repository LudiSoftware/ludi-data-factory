import requests
from urllib.parse import quote
from FM.FMDb import FMDB
import Utils

client = FMDB(ip="192.168.1.166", port=27017)
db = client.database("usysr").collection("organizations")

maps = "AIzaSyALaLmm6sXkyAYeWbd-szSCLFvmogH9BRM"
api_key = "AIzaSyBM2Uw53v9kTQRRyLITxu52ZjhNpDusJDI"
location = "33.5186,-86.8104" # lat,long for San Francisco
radius = 10000 # search radius in meters


type = "sports"
url_type = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&key={api_key}"

query = "alabama soccer association"
url_query = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={quote(query)}&key={api_key}"



response = requests.get(url_query)
results = response.json()["results"]

""" Prepare Results for DB """
prepared_results = []
for result in results:
    loc = result["geometry"]["location"]
    lat = loc["lat"]
    lng = loc["lng"]
    csz = Utils.latlng_to_citystate(lat, lng)
    result["csz"] = csz
    result["category"] = type
    prepared_results.append(result)
    print(result["name"])

db.add_records_field_match(prepared_results, "name")