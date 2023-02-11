import uuid
import time
from Firebase.FirebaseAdmin import FireDB


class League:
    def __init__(self):
        self.id = str(uuid.uuid1())
        self.date_created = str(time.time())
        self.name = "unassigned"
        self.details = "unassigned"
        self.owner_id = "unassigned"
        self.owner_name = "unassigned"
        self.organization_id = "unassigned"
        self.organization_ids = []
        self.address_one = "unassigned"
        self.address_two = "unassigned"
        self.city = "unassigned"
        self.state = "unassigned"
        self.zip = "unassigned"
        self.img_url = "unassigned"
        self.sport = "soccer"
        self.type = "unassigned"
        self.sub_type = "unassigned"
        self.has_review = False
        self.reviews = []

    def save_to_firebase(self):
        db = FireDB("leagues")
        db.add_object(self.id, self.__dict__)

    def get_city_state_zip(self):
        return f"{self.city}, {self.state} {self.zip}"
