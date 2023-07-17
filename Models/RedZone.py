import time
import uuid

newLatLng = lambda lat, lng: {"latitude": lat, "longitude": lng}
class LudiLatLng:
        def __init__(self, lat:float=0.0, lng:float=0.0):
            self.latitude = lat
            self.longitude = lng

class RedZone:
    def __init__(self, redzone={}):
        self.id = redzone.get('id', str(uuid.uuid4()))
        self.dateCreated = redzone.get('dateCreated', str(time.time()))
        self.dateUpdated = redzone.get('dateUpdated', str(time.time()))
        self.name = redzone.get('name', "")
        self.description = redzone.get('description', "")
        self.latLngs = redzone.get('latLngs', [])
        self.isOpen = redzone.get('isOpen', True)
        self.locationIds = redzone.get('locationId', "")
        self.state = redzone.get('state', "")

    def toJson(self):
        return {
            "id": self.id,
            "dateCreated": self.dateCreated,
            "dateUpdated": self.dateUpdated,
            "name": self.name,
            "description": self.description,
            "latLngs": self.latLngs,
            "isOpen": self.isOpen,
            "locationIds": self.locationIds,
            "state": self.state
        }




