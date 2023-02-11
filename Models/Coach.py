from Firebase.FirebaseAdmin import FireDB
from Models.User import User
db = FireDB()
UNASSIGNED = "unassigned"
class Coach:
    ORDER_BY_ORGANIZATION = "organizationId"

    def __init__(self, _id=None, firebase_user=None):
        self.owner_id = firebase_user.get('id') if firebase_user else UNASSIGNED
        self.owner_name = firebase_user.get('name') if firebase_user else UNASSIGNED
        self.organization_id = UNASSIGNED
        self.organization_name = UNASSIGNED
        self.organization_ids = []
        self.address_one = UNASSIGNED
        self.address_two = UNASSIGNED
        self.city = UNASSIGNED
        self.state = UNASSIGNED
        self.zip = UNASSIGNED
        self.sport = "soccer"
        self.sub_type = UNASSIGNED
        self.details = UNASSIGNED
        self.is_free = False
        self.teams = []
        self.has_review = False
        self.reviews = []
        self.rating_score = UNASSIGNED
        self.rating_count = UNASSIGNED
        self.review_answer_count = UNASSIGNED
        self.review_details = UNASSIGNED

    def save_coach_to_firebase(self):
        return db.add_object(self.owner_id, self.__dict__, collection="coaches")

    @staticmethod
    def get_user_by_id(user_id, parseToCoach=True):
        json_user = db.get_object(user_id, collection="users")[0][user_id]
        if not parseToCoach:
            return json_user
        newCoach = Coach(firebase_user=json_user)
        return newCoach

if __name__ == '__main__':
    t = Coach.get_user_by_id("tnmjTR7r1HPwIaBb2oXrDrwXT842", parseToCoach=True)
    print(t.save_coach_to_firebase())