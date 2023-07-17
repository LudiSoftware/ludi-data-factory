from Models.RedZone import RedZone
from Models.RedZone import newLatLng
from YsrDB import FireDB

db = FireDB("redzones")

newRedZone = {
                "name": "BIIIitttcccchhhhh",
                "description": "michael is gay?",
                "latLngs": [newLatLng(0.0, 0.0), newLatLng(0.0, 0.0), newLatLng(0.0, 0.0)]
              }

redzone = RedZone(newRedZone)
db.add_object(redzone.id, redzone.toJson())
