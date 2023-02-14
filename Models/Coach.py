import time

UNASSIGNED = "unassigned"
class Coach:

    def __init__(self, _id=None, firebase_user=None):
        if firebase_user and type(firebase_user) not in [dict]:
            firebase_user = firebase_user.__dict__
        self.dateCreated = firebase_user.get('dateCreated', str(time.time()))
        self.dateUpdated = firebase_user.get('dateUpdated', str(time.time()))
        self.ownerId = firebase_user.get('id') if firebase_user else UNASSIGNED
        self.ownerName = firebase_user.get('name') if firebase_user else UNASSIGNED
        self.imgUrl = UNASSIGNED
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

