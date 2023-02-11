import uuid
import time
from Firebase.FirebaseAdmin import FireDB


class Organization:

    ORDER_BY_SPORTS = "sport"
    UNASSIGNED = "unassigned"

    def __init__(self, place_dict=None):
        self.id = str(uuid.uuid1())
        self.dateCreated = str(time.time())
        self.name = self.UNASSIGNED
        self.addressOne = self.UNASSIGNED
        self.addressTwo = self.UNASSIGNED
        self.city = self.UNASSIGNED
        self.state = self.UNASSIGNED
        self.zip = self.UNASSIGNED
        self.latitude = self.UNASSIGNED
        self.longitude = self.UNASSIGNED
        self.sport = "soccer"
        self.type = self.UNASSIGNED
        self.subType = self.UNASSIGNED
        self.ratingScore = "0.0"
        self.ratingCount = "0"
        self.details = self.UNASSIGNED
        self.officeHours = self.UNASSIGNED
        self.websiteUrl = self.UNASSIGNED
        self.imgOrgIconUri = self.UNASSIGNED
        self.managerId = self.UNASSIGNED
        self.managerName = self.UNASSIGNED
        self.estMemberCount = self.UNASSIGNED
        self.estStaffCount = self.UNASSIGNED
        self.business_status = "UNKNOWN"
        self.fromGoogle = False
        self.staffIds = []
        self.reviewIds = []
        self.leagueIds = []
        self.regionIds = []
        self.locationIds = []
        self.imgUris = []
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


