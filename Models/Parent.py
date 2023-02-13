
UNASSIGNED = "unassigned"
class Parent:

    def __init__(self, _id=None, firebase_user=None):
        if firebase_user and type(firebase_user) not in [dict]:
            firebase_user = firebase_user.__dict__
        self.ownerId = firebase_user.get('id') if firebase_user else UNASSIGNED
        self.ownerName = firebase_user.get('name') if firebase_user else UNASSIGNED
        self.imgUrl = UNASSIGNED
        self.details = UNASSIGNED
        self.isFree = False
        self.hasReview = False
        self.reviews = []
        self.ratingScore = UNASSIGNED
        self.ratingCount = UNASSIGNED
        self.reviewAnswerCount = UNASSIGNED
        self.reviewDetails = UNASSIGNED
        self.player = False
        self.playerIds = []
        self.team = False
        self.teamIds = []
        self.organizationIds = []
