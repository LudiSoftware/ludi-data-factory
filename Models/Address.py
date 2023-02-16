

class Address:
    def __init__(self, json_data=None):
        self.name = json_data.get('name', None)
        self.addressOne = json_data.get('addressOne', None)
        self.addressTwo = json_data.get('addressTwo', None)
        self.city = json_data.get('city', None)
        self.state = json_data.get('state', None)
        self.zip = json_data.get('zip', None)
        self.latitude = json_data.get('latitude', None)
        self.longitude = json_data.get('longitude', None)

    def from_places(self, places_data):
        self.name = places_data.get('name', None)
        self.addressOne = places_data.get('formatted_address', None)
        self.addressTwo = places_data.get('addressTwo', None)
        self.city = places_data.get('csz')[0]
        self.state = places_data.get('csz')[1]
        self.zip = places_data.get('csz')[2]
        temp = places_data.get('geometry')["location"]
        self.latitude = str(temp["lat"])
        self.longitude = str(temp["lng"])