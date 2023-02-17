import time
import uuid

UNASSIGNED = "unassigned"


class CoachRef:
    def __init__(self, coach: dict = {}):
        self.coachId = coach.get('coachId', None)
        self.name = coach.get('name', None)
        self.title = coach.get('title', None)

class Coach:

    def __init__(self, firebase_user=None):
        if firebase_user and type(firebase_user) not in [dict]:
            firebase_user = firebase_user.__dict__
        self.id = firebase_user.get('id', uuid.uuid4())
        self.title = firebase_user.get('title', None)
        self.organizationRefs = firebase_user.get('organizationRefs', None)
        self.teamRefs = firebase_user.get('teamRefs', None)
        self.hasReview = firebase_user.get('hasReview', False)
        self.reviewBundle = firebase_user.get('reviewBundle', None)
        self.dateCreated = firebase_user.get('dateCreated', time.time())
        self.dateUpdated = firebase_user.get('dateUpdated', time.time())
        self.name = firebase_user.get('name', None)
        self.firstName = firebase_user.get('firstName', None)
        self.lastName = firebase_user.get('lastName', None)
        self.type = firebase_user.get('type', None)
        self.subType = firebase_user.get('subType', None)
        self.details = firebase_user.get('details', None)
        self.isFree = firebase_user.get('isFree', False)
        self.status = firebase_user.get('status', None)
        self.mode = firebase_user.get('mode', None)
        self.imgUrl = firebase_user.get('imgUrl', None)
        self.sport = firebase_user.get('sport', None)
        self.chatEnabled = firebase_user.get('chatEnabled', False)


