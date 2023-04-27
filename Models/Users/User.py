import uuid
import time

from Models.TestDataCreator.TestData import DataGeneration as dg
dg = dg()
UNASSIGNED = "unassigned"
BASIC_USER = "basic"
PARENT_USER = "parent"
PLAYER_USER = "player"
COACH_USER = "coach"
CLOSED = "closed"



class User:
    def __init__(self, _id=None, firebase_user={}):
        self.id = firebase_user.get("id", _id if _id else str(uuid.uuid4()))
        self.dateCreated = firebase_user.get("dateCreated", str(time.time()))
        self.dateUpdated = firebase_user.get("dateUpdated", str(time.time()))
        self.username = firebase_user.get("username", dg.generate_username())
        fakeName = dg.generate_full_name()
        self.name = firebase_user.get("name", fakeName)
        self.firstName = firebase_user.get("firstName", dg.get_first_name(fakeName))
        self.lastName = firebase_user.get("lastName", dg.get_last_name(fakeName))
        self.email = firebase_user.get("email", dg.generate_email())
        self.phone = firebase_user.get("phone", dg.generate_phone_number())
        fakeBirthday = dg.generate_birthday()
        self.age = firebase_user.get("age", dg.get_age_for_birthday(fakeBirthday))
        self.dob = firebase_user.get("dob", fakeBirthday)
        self.gender = firebase_user.get("gender", "male")
        self.auth = firebase_user.get("auth", "basic")
        self.type = firebase_user.get("type", "basic")
        self.subType = firebase_user.get("subType", "basic")
        self.details = firebase_user.get("details", "no details")
        self.visibility = firebase_user.get("visibility", "open")
        self.photoUrl = firebase_user.get("photoUrl", "")
        self.emailVerified = firebase_user.get("emailVerified", False)
        self.parent = firebase_user.get("parent", False)
        self.player = firebase_user.get("player", False)
        self.coach = firebase_user.get("coach", False)
        self.valid = firebase_user.get("valid", True)


    def createAndSaveUser(self, userId: str):
        from Firebase.FirebaseAdmin import FireDB
        self.id = userId
        fb = FireDB()
        fb.add_object(collection="users", obj_id=self.id, obj=self.__dict__)
        return self.id


if __name__ == '__main__':
    u = User()
    u.createAndSaveUser("GMTRmTSP4hUSCG0Owk7D6EDfeAx2")
