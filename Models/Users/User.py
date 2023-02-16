import uuid
import time

UNASSIGNED = "unassigned"
BASIC_USER = "basic"
PARENT_USER = "parent"
PLAYER_USER = "player"
COACH_USER = "coach"
CLOSED = "closed"

class User:
    def __init__(self, _id=None, firebase_user=None):
        self.id = str(uuid.uuid1()) if not _id else str(_id)
        self.dateCreated = str(time.time())
        self.dateUpdated = str(time.time())
        self.username = UNASSIGNED
        self.name = UNASSIGNED
        self.firstName = UNASSIGNED
        self.lastName = UNASSIGNED
        self.auth = BASIC_USER
        self.type = UNASSIGNED
        self.subType = UNASSIGNED
        self.details = UNASSIGNED
        self.email = UNASSIGNED
        self.phone = UNASSIGNED
        self.age = UNASSIGNED
        self.gender = UNASSIGNED
        self.visibility = CLOSED
        self.photoUrl = UNASSIGNED
        self.emailVerified = False
        self.parent = False
        self.player = False
        self.coach = False
        self.valid = None
        if firebase_user:
            self.parse(firebase_user)

    def parse(self, data:{}):
        self.auth = data.get('auth')
        self.dateCreated = data.get('dateCreated')
        self.dateUpdated = data.get('dateUpdated')
        self.email = data.get('email')
        self.emailVerified = data.get('emailVerified', False)
        self.id = data.get('id')
        self.name = data.get('name')
        self.age = data.get('age')
        self.phone = data.get('phone')
        self.photoUrl = data.get('photoUrl')
        self.type = data.get('type')
        self.subType = data.get('subType')
        self.username = data.get('username')
        self.valid = data.get('valid', False)
        self.visibility = data.get('visibility', False)
        self.coach = data.get('coach', False)
        self.parent = data.get('parent', False)
        self.player = data.get('player', False)
