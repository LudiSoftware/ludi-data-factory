import uuid
from Firebase.FirebaseAdmin import FireDB
from Models import Base
from FM.FMDb import FMDB



class Place:
    def __init__(self, place_dict):
        self._id = place_dict.get('_id')
        self.google_place_business_status = place_dict.get('business_status')
        self.geometry = place_dict.get('geometry')
        self.google_place_icon = place_dict.get('icon')
        self.icon_background_color = place_dict.get('icon_background_color')
        self.icon_mask_base_uri = place_dict.get('icon_mask_base_uri')
        self.google_place_name = place_dict.get('name')
        # self.opening_hours = place_dict.get('opening_hours')
        self.google_place_photos = place_dict.get('photos')
        self.google_place_id = place_dict.get('place_id')
        # self.plus_code = place_dict.get('plus_code')
        self.google_place_rating = place_dict.get('rating')
        # self.reference = place_dict.get('reference')
        self.google_place_scope = place_dict.get('scope')
        self.google_place_types = place_dict.get('types')
        self.google_place_user_ratings_total = place_dict.get('user_ratings_total')
        self.google_place_address = place_dict.get('vicinity')
        self.google_place_csz = place_dict.get('csz')
        self.google_place_category = place_dict.get('category')


class Location(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ludi
        self.sports = kwargs.get('sport', ["soccer"])
        self.fields = kwargs.get('fields', ["2B", "2A"])
        self.address = kwargs.get('address', "1234 Main St")
        self.imgUris = kwargs.get('imgUris', [])
        self.parkingInfo = kwargs.get("parkingInfo", "Park down on the gravel") #// "Park on the third spot to the right"
        self.estPeople = kwargs.get('estPeople', 0)
        self.managerIds = kwargs.get('managerIds', [str(uuid.uuid1())])
        self.organizationRefs = kwargs.get('organizationRefs', [])
        self.hasReview = kwargs.get('hasReview', False)
        self.reviewBundle = kwargs.get('reviewBundle', {})
        # google
        self.googlePlaceBusinessStatus = kwargs.get('business_status', "None")
        geometry = kwargs.get('geometry', "None")
        loc = geometry.get('location', "None")
        self.googlePlaceLat = str(loc.get('lat', "None"))
        self.googlePlaceLng = str(loc.get('lng', "None"))
        self.googlePlaceIcon = kwargs.get('icon', "None")
        self.iconBackgroundColor = kwargs.get('icon_background_color', "None")
        self.iconMaskBaseUri = kwargs.get('icon_mask_base_uri', "None")
        self.googlePlaceName = kwargs.get('name', "None")
        self.googlePlacePhotos = str(kwargs.get('photos', "None"))
        self.googlePlaceId = kwargs.get('place_id', "None")
        self.googlePlaceRating = str(kwargs.get('rating', "None"))
        self.googlePlaceScope = kwargs.get('scope', "None")
        self.googlePlaceTypes = kwargs.get('types', "None")
        self.googlePlaceUserRatingsTotal = kwargs.get('user_ratings_total', "None")
        self.googlePlaceAddress = kwargs.get('vicinity', "None")
        self.googlePlaceCsz = str(kwargs.get('csz', "None"))
        self.googlePlaceCategory = kwargs.get('category', "None")

    def save_to_firebase(self):
        db = FireDB("locations")
        db.add_object(self.id, self.__dict__)


client = FMDB(ip="192.168.1.166", port=27017)
db = client.database("usysr").collection("locations")

results = db.base_query({})
for r in results:
    loc = Location(**r)
    loc.save_to_firebase()
