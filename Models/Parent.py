from Models.User import User


class Parent(User):
    ORDER_BY_ORGANIZATION = "organizationId"

    def __init__(self, _id=None):
        super().__init__(_id=_id)
        self.name = ""
        self.imgUrl = ""
        self.organizationIds = []
        self.sport = "unassigned"
        self.type = "unassigned"
        self.subType = "unassigned"
        self.details = ""
        self.email = ""
        self.phone = ""
        self.isFree = False
        self.hasReview = False
        self.reviews = []
        self.ratingScore = ""
        self.ratingCount = ""
        self.reviewAnswerCount = ""
        self.reviewDetails = ""
