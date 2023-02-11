from Models.User import User

class Team(User):
    ORDER_BY_ORGANIZATION = "organizationId"

    def __init__(self):
        super().__init__()
        self.headCoachId = self.UNASSIGNED
        self.headCoachName = self.UNASSIGNED
        self.coachIds = []
        self.managerId = self.UNASSIGNED
        self.managerName = self.UNASSIGNED
        self.organizationId = self.UNASSIGNED
        self.organizationName = self.UNASSIGNED
        self.organizationIds = []
        self.sport = "soccer"
        self.year = self.UNASSIGNED
        self.ageGroup = self.UNASSIGNED
        self.isActive = False
        self.gender = self.UNASSIGNED
        self.type = self.UNASSIGNED
        self.subType = self.UNASSIGNED
        self.details = self.UNASSIGNED
        self.isFree = False
        self.mode = "viewonly"
        self.hasReview = False
        self.reviews = []
        self.ratingScore = self.UNASSIGNED
        self.ratingCount = self.UNASSIGNED
        self.reviewAnswerCount = self.UNASSIGNED
        self.reviewDetails = self.UNASSIGNED
