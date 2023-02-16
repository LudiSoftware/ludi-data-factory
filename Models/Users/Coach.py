import time


UNASSIGNED = "unassigned"




class CoachNote:
    def __init__(self, obj):
        self.id = obj.get("id", None)
        self.dateCreated = obj.get("dateCreated", None)
        self.dateUpdated = obj.get("dateUpdated", None)
        self.coachId = obj.get("coachId", None)
        self.aboutTeamId = obj.get("aboutTeamId", None)
        self.aboutPlayerId = obj.get("aboutPlayerId", None)
        self.message = obj.get("message", None)


class CoachRef:
    def __init__(self, coach: dict = {}):
        self.coachId = coach.get('coachId', None)
        self.name = coach.get('name', None)
        self.title = coach.get('title', None)

class Coach:

    def __init__(self, _id=None, firebase_user=None):
        if firebase_user and type(firebase_user) not in [dict]:
            firebase_user = firebase_user.__dict__
        self.dateCreated = firebase_user.get('dateCreated', str(time.time()))
        self.dateUpdated = firebase_user.get('dateUpdated', str(time.time()))
        self.id = firebase_user.get('id') if firebase_user else UNASSIGNED
        self.name = firebase_user.get('name') if firebase_user else UNASSIGNED
        self.imgUrl = UNASSIGNED

        self.organizationRefs: [] = []
        self.teamRefs: [] = []
        self.hasReview = False
        self.reviewBundle = None

        self.organizationId = UNASSIGNED
        self.organizationName = UNASSIGNED
        self.organizationIds = []
        self.addressOne = UNASSIGNED
        self.addressTwo = UNASSIGNED
        self.city = UNASSIGNED
        self.state = UNASSIGNED
        self.zip = UNASSIGNED
        self.sport = "soccer"
        self.details = UNASSIGNED
        self.isFree = False
        self.teams = []
        self.hasReview = False
        self.reviews = []
        self.ratingScore = UNASSIGNED
        self.ratingCount = UNASSIGNED
        self.reviewAnswerCount = UNASSIGNED
        self.reviewDetails = UNASSIGNED

