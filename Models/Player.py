
UNASSIGNED = "unassigned"
class Player:

    def __init__(self, _id=None, firebase_user=None):
        if firebase_user and type(firebase_user) not in [dict]:
            firebase_user = firebase_user.__dict__
        self.ownerId = firebase_user.get('id') if firebase_user else UNASSIGNED
        self.ownerName = firebase_user.get('name') if firebase_user else UNASSIGNED
        self.tryoutNumber = UNASSIGNED
        self.position = UNASSIGNED
        self.teamId = UNASSIGNED
        self.teamName = UNASSIGNED
        self.teamIds = []
        self.organizationId = UNASSIGNED
        self.organizationName = UNASSIGNED
        self.organizationIds = []
        self.sport = "soccer"
        self.isFree = False
        self.hasReview = False
        self.reviewIds = []
        self.ratingScore = UNASSIGNED
        self.ratingCount = UNASSIGNED
        self.reviewAnswerCount = UNASSIGNED
        self.reviewDetails = UNASSIGNED