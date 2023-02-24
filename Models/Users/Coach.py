import time
import uuid


from Models.TestDataCreator.TestData import DataGeneration as dg
dg = dg()

UNASSIGNED = "unassigned"


class CoachRef:
    def __init__(self, user_or_coach_json: dict = {}):
        self.id = user_or_coach_json.get('id', str(uuid.uuid4()))
        self.coachId = user_or_coach_json.get('coachId', self.id)
        self.name = user_or_coach_json.get('name', dg.generate_full_name())
        self.isHeadCoach = user_or_coach_json.get('isHeadCoach', True)
        self.title = user_or_coach_json.get('title', "Head Coach")
        self.imgUrl = user_or_coach_json.get('imgUrl', dg.generate_coach_img_url())

class Coach:

    def __init__(self, firebase_user=None):
        if firebase_user and type(firebase_user) not in [dict]:
            firebase_user = firebase_user.__dict__
        self.id = firebase_user.get('id', str(uuid.uuid4()))
        self.title = firebase_user.get('title', "Head Coach")
        self.organizations = firebase_user.get('organizations', [])
        self.teams = firebase_user.get('teams', [])
        self.evaluations = firebase_user.get('evaluations', [])
        self.hasReview = firebase_user.get('hasReview', False)
        self.reviewBundle = firebase_user.get('reviewBundle', "None")
        #base
        self.dateCreated = firebase_user.get('dateCreated', str(time.time()))
        self.dateUpdated = firebase_user.get('dateUpdated', str(time.time()))
        fakeName = dg.generate_full_name()
        self.name = firebase_user.get('name', fakeName)
        self.firstName = firebase_user.get('firstName', dg.get_first_name(fakeName))
        self.lastName = firebase_user.get('lastName', dg.get_last_name(fakeName))
        self.type = firebase_user.get('type', "competitive")
        self.subType = firebase_user.get('subType', "youth")
        self.details = firebase_user.get('details', "None")
        self.isFree = firebase_user.get('isFree', False)
        self.status = firebase_user.get('status', "active")
        self.mode = firebase_user.get('mode', "active")
        self.imgUrl = firebase_user.get('imgUrl', dg.generate_coach_img_url())
        self.sport = firebase_user.get('sport', "Soccer")


