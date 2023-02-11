import uuid
import time
import json


from Firebase.FirebaseAdmin import FireDB

class User:
    UNASSIGNED = "unassigned"
    BASIC_USER = "basic"
    PARENT_USER = "parent"
    PLAYER_USER = "player"
    COACH_USER = "coach"
    CLOSED = "closed"

    def __init__(self, _id=None, firebase_user=None):
        self.id = str(uuid.uuid1()) if not _id else str(_id)
        self.dateCreated = str(time.time())
        self.dateUpdated = str(time.time())
        self.username = self.UNASSIGNED
        self.name = self.UNASSIGNED
        self.lastName = self.UNASSIGNED
        self.auth = self.BASIC_USER
        self.type = self.UNASSIGNED
        self.subType = self.UNASSIGNED
        self.details = self.UNASSIGNED
        self.email = self.UNASSIGNED
        self.phone = self.UNASSIGNED
        self.age = self.UNASSIGNED
        self.gender = self.UNASSIGNED
        self.visibility = self.CLOSED
        self.photoUrl = self.UNASSIGNED
        self.email_verified = False
        self.parent_id = self.UNASSIGNED
        self.player_id = self.UNASSIGNED
        self.coach_id = self.UNASSIGNED
        self.organization = self.UNASSIGNED
        self.organization_id = self.UNASSIGNED
        self.coachUser = None
        self.basicUser = None
        self.valid = None
        if firebase_user:
            self.parse(firebase_user)

    def parse(self, data:{}):
        self.auth = data.get('auth')
        self.basicUser = data.get('basicUser')
        self.coachUser = data.get('coachUser')
        self.dateCreated = data.get('dateCreated')
        self.dateUpdated = data.get('dateUpdated')
        self.email = data.get('email')
        self.email_verified = data.get('emailVerified')
        self.id = data.get('id')
        self.name = data.get('name')
        self.organization = data.get('organization')
        self.phone = data.get('phone')
        self.photoUrl = data.get('photoUrl')
        self.type = data.get('type')
        self.username = data.get('username')
        self.valid = data.get('valid')
        self.visibility = data.get('visibility')

    def save_to_firebase(self):
        db = FireDB("users")
        db.add_object(self.id, self.__dict__)

    @staticmethod
    def get_user_by_id(user_id, parse=True):
        db = FireDB("users")
        json_user = db.get_object(user_id)[0][user_id]
        if not parse:
            return json_user
        newUser = User(firebase_user=json_user)
        return newUser

if __name__ == '__main__':
    t = User.get_user_by_id("tnmjTR7r1HPwIaBb2oXrDrwXT842", parse=True)
    print(t)