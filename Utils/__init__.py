from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

def latlng_to_citystate(lat, lng):
    try:
        location = geolocator.reverse(f"{lat}, {lng}", exactly_one=True)
        address = location.raw['address']
        city = address.get('town', address.get('city', ''))
        state = address.get('state', '')
        zipcode = address.get('postcode', '')
        return (city, state, zipcode)
    except Exception as e:
        print(e)
        return (None, None, None)

