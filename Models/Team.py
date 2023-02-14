import uuid
import time

from Firebase.FirebaseAdmin import FireDB

UNASSIGNED = "unassigned"
db = FireDB()
class Team:

    def __init__(self):
        super().__init__()
        self.id = str(uuid.uuid1())
        self.dateCreated = str(time.time())
        self.dateUpdated = str(time.time())
        self.headCoachId = "tnmjTR7r1HPwIaBb2oXrDrwXT842"
        self.headCoachName = "Lucas Romeo"
        self.coachIds = ["tnmjTR7r1HPwIaBb2oXrDrwXT842", "uuid2", "uuid3"]
        self.managerId = UNASSIGNED
        self.managerName = UNASSIGNED
        self.managerIds = ["none"]
        self.organizationId = UNASSIGNED
        self.organizationName = UNASSIGNED
        self.organizationIds = ["none"]
        self.roster = ["none"]
        self.name = "Team Bitches One"
        self.sport = "soccer"
        self.year = "2007"
        self.ageGroup = "U15"
        self.isActive = False
        self.gender = "male"
        self.type = UNASSIGNED
        self.subType = UNASSIGNED
        self.details = UNASSIGNED
        self.isFree = False
        self.mode = "viewonly"
        self.status = "active"
        self.hasReview = False
        self.reviews = ["none"]
        self.ratingScore = UNASSIGNED
        self.ratingCount = UNASSIGNED
        self.reviewAnswerCount = UNASSIGNED
        self.reviewDetails = UNASSIGNED

    def saveToFirebase(self):
        return db.add_object(self.id, self.__dict__, collection="teams")

if __name__ == '__main__':
    newTeam = Team()
    newTeam.saveToFirebase()