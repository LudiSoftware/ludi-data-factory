from Models.User import User


class Player(User):
    ORDER_BY_ORGANIZATION = "organizationId"

    def __init__(self, _id=None):
        super().__init__(_id=_id)
        self.ownerId = self.id
        self.ownerName = self.name
        self.position = self.UNASSIGNED
        self.teamId = self.UNASSIGNED
        self.teamName = self.UNASSIGNED
        self.teamIds = []
        self.organizationId = self.UNASSIGNED
        self.organizationName = self.UNASSIGNED
        self.organizationIds = []
        self.sport = "soccer"
        self.isFree = False
        self.hasReview = False
        self.reviewIds = []
        self.ratingScore = self.UNASSIGNED
        self.ratingCount = self.UNASSIGNED
        self.reviewAnswerCount = self.UNASSIGNED
        self.reviewDetails = self.UNASSIGNED