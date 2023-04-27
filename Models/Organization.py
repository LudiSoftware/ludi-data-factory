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
        # Main (3) TOTAL (37)
        self.id = obj.get('id', str(uuid.uuid4()))
        self.officeHours = obj.get('officeHours', "8am-5pm")
        self.websiteUrl = obj.get('websiteUrl', "www.ludisportsapp.com")
        # Counts (3)
        self.estMemberCount = obj.get('estMemberCount', 0)
        self.estStaffCount = obj.get('estStaffCount', 0)
        self.estTeamCount = obj.get('estTeamCount', 0)
        # References (5)
        self.staff = obj.get('staff', [])
        self.coaches = obj.get('coaches', [])
        self.leagues = obj.get('leagues', [])
        self.teams = obj.get('teams', [])
        self.regions = obj.get('regions', [])
        # Locations (1)
        self.locations = obj.get('locations', [])
        # Images (2)
        self.imgUris = obj.get('imgUris', [])
        self.imgOrgIconUri = obj.get('imgOrgIconUri', "None")
        # Ratings/Reviews (3)
        self.reviews = obj.get('reviews', [])
        self.ratingScore = obj.get('ratingScore', 0)
        self.ratingCount = obj.get('ratingCount', 0)
        # Google Specific (8)
        self.fromGoogle = obj.get('fromGoogle', False)
        self.google_place_category = obj.get('google_place_category', "None")
        self.business_status = obj.get('business_status', "None")
        self.google_place_icon = obj.get('google_place_icon', "None")
        self.google_place_rating = obj.get('google_place_rating', "None")
        self.google_place_id = obj.get('google_place_id', "None")
        self.google_place_user_ratings_total = obj.get('google_place_user_ratings_total', "None")
        self.tags = obj.get('tags', [])
        # Base (12)
        self.dateCreated = obj.get('dateCreated', str(time.time()))
        self.dateUpdated = str(time.time())
        self.name = obj.get('name', "Luda Youth Soccer Club")
        self.type = obj.get('type', "youth sports organization")
        self.subType = obj.get('subType', "soccer club")
        self.details = obj.get('details', "A full search for-profit soccer club")
        self.isFree = obj.get('isFree', False)
        self.status = obj.get('status', "open")
        self.mode = obj.get('mode', "open")
        self.imgUrl = obj.get('imgUrl', "")
        self.sport = obj.get('sport', "soccer")
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
        count = 0
        if str(category) == "soccer":
            if count > 10: break
            count += 1
            newOrg = Organization(item)
            newOrgDict = newOrg.__dict__
            orgs.append(newOrgDict)
            fire.add_object(newOrg.id, newOrgDict)


