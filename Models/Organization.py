import uuid
import time
from Firebase.FirebaseAdmin import FireDB
from Models.Address import Address
from Models.Users.Coach import CoachRef

ORDER_BY_SPORTS = "sport"
UNASSIGNED = "unassigned"

class OrganizationRef:
    id: str = None
    organizationId: str = None
    name: str = None
    
class Organization:

    def __init__(self, obj=None, place_dict=None):
        self.id = obj.get('id', uuid.uuid4())
        self.ratingScore = obj.get('ratingScore', None)
        self.ratingCount = obj.get('ratingCount', None)
        self.officeHours = obj.get('officeHours', None)
        self.websiteUrl = obj.get('websiteUrl', None)
        self.imgOrgIconUri = obj.get('imgOrgIconUri', None)
        self.managerId = obj.get('managerId', None)
        self.managerName = obj.get('managerName', None)
        self.estMemberCount = obj.get('estMemberCount', None)
        self.estStaffCount = obj.get('estStaffCount', None)
        self.staff = obj.get('staff', [CoachRef])
        self.reviews = obj.get('reviews', [str])
        self.leagues = obj.get('leagues', [])
        self.regions = obj.get('regions', [str])
        self.locations = obj.get('locations', [])
        self.imgUris = obj.get('imgUris', [str])
        self.fromGoogle = obj.get('fromGoogle', False)
        self.google_place_category = obj.get('google_place_category', None)
        self.business_status = obj.get('business_status', None)
        self.google_place_icon = obj.get('google_place_icon', None)
        self.google_place_rating = obj.get('google_place_rating', None)
        self.tags = obj.get('tags', None)
        self.google_place_id = obj.get('google_place_id', None)
        self.google_place_user_ratings_total = obj.get('google_place_user_ratings_total', None)
        self.dateCreated = time.time()
        self.dateUpdated = time.time()
        self.name = obj.get('name', None)
        self.firstName = obj.get('firstName', None)
        self.lastName = obj.get('lastName', None)
        self.type = obj.get('type', None)
        self.subType = obj.get('subType', None)
        self.details = obj.get('details', None)
        self.isFree = obj.get('isFree', False)
        self.status = obj.get('status', None)
        self.mode = obj.get('mode', None)
        self.imgUrl = obj.get('imgUrl', None)
        self.sport = obj.get('sport', None)
        self.chatEnabled = obj.get('chatEnabled', False)
        if place_dict:
            self.business_status = place_dict.get('business_status')
            self.google_place_icon = place_dict.get('icon')
            self.name = place_dict.get('name')
            self.google_place_photos = place_dict.get('photos')
            self.google_place_id = place_dict.get('place_id')
            self.google_place_rating = str(place_dict.get('rating'))
            self.google_place_user_ratings_total = str(place_dict.get('user_ratings_total'))
            self.ratingScore = str(self.google_place_rating)
            self.ratingCount = str(self.google_place_user_ratings_total)
            self.tags = str(place_dict.get('types'))
            self.addressOne = place_dict.get('formatted_address')
            self.csz = str(place_dict.get('csz'))
            self.city = place_dict.get('csz')[0]
            self.state = place_dict.get('csz')[1]
            self.zip = place_dict.get('csz')[2]
            temp = place_dict.get('geometry')["location"]
            self.latitude = str(temp["lat"])
            self.longitude = str(temp["lng"])
            self.address = Address().from_places(place_dict)
            self.google_place_category = place_dict.get('category')
            self.sport = self.google_place_category
            self.fromGoogle = True

    def save_to_firebase(self):
        db = FireDB("organizations")
        db.add_object(self.id, self.__dict__)



if __name__ == '__main__':
    from FM.FMDb import FMDB
    from F import DICT
    fire = FireDB("organizations")
    client = FMDB(ip="192.168.1.166", port=27017)
    db = client.database("usysr").collection("organizations")
    results = db.base_query({})
    orgs = []
    for item in results:
        print(item)
        category = DICT.get("category", item, "nope")
        if str(category) == "soccer":
            newOrg = Organization(item)
            newOrgDict = newOrg.__dict__
            orgs.append(newOrgDict)
            fire.add_object(newOrg.id, newOrgDict)


