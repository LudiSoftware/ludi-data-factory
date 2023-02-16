import uuid
import time

from Firebase.FirebaseAdmin import FireDB
from Models.Users.Coach import CoachRef
from Models.Users.Player import PlayerRef

UNASSIGNED = "unassigned"
db = FireDB()


class TeamRef:
    teamId: str = None
    name: str = None
    sport: str = None
    status: str = None

class Team:

    def __init__(self, team_obj={}):
        self.id = team_obj.get('teamId', uuid.uuid1())
        self.headCoachId = team_obj.get('headCoachId', "tnmjTR7r1HPwIaBb2oXrDrwXT842")
        self.headCoachName = team_obj.get('headCoachName', "Phil Yagota")
        self.coachRefs: [] = team_obj.get('coachRefs', []) if isinstance(team_obj.get('coachRefs', None), list) else None
        self.managerRefs: [] = team_obj.get('managerRefs', []) if isinstance(team_obj.get('managerRefs', None), list) else None
        self.organizationRefs: [] = team_obj.get('organizationRefs', []) if isinstance(team_obj.get('organizationRefs', None), list) else None
        self.roster = team_obj.get('roster', [PlayerRef]) if isinstance(team_obj.get('roster', None), list) else None
        self.name = team_obj.get('name', "The First YSR Team")
        self.firstName = team_obj.get('firstName', "Phil")
        self.lastName = team_obj.get('lastName', "Yagota")
        self.year = team_obj.get('year', "2008")
        self.ageGroup = team_obj.get('ageGroup', "U15")
        self.isActive = team_obj.get('isActive', True)
        self.gender = team_obj.get('gender', "male")
        self.imgUrl = team_obj.get('imgUrl', "")
        self.sport = team_obj.get('sport', "soccer")
        self.hasReview = team_obj.get('hasReview', False)
        self.reviews = team_obj.get('reviews', None)
        self.dateCreated = team_obj.get('dateCreated', time.time())
        self.dateUpdated = team_obj.get('dateUpdated', time.time())
        self.type = team_obj.get('type', None)
        self.subType = team_obj.get('subType', None)
        self.details = team_obj.get('details', None)
        self.isFree = team_obj.get('isFree', False)
        self.status = team_obj.get('status', None)
        self.mode = team_obj.get('mode', None)


    def saveToFirebase(self):
        return db.add_object(self.id, self.__dict__, collection="teams")

    def makeNewTeam(self):
        newRef = CoachRef({"id": "tnmjTR7r1HPwIaBb2oXrDrwXT842",
                           "name": "Phil Yagota", "title": "Head Coach"})
        self.name = "The First YSR Team"
        self.headCoachId = "tnmjTR7r1HPwIaBb2oXrDrwXT842"
        self.headCoachName = "Phil Yagota"
        self.coachRefs = [newRef]
        return self


if __name__ == '__main__':
    newTeam = Team()
    newTeam.saveToFirebase()