import uuid
import time

# from Firebase.FirebaseAdmin import FireDB

from Models.TestDataCreator.TestData import DataGeneration as dg
dg = dg()

stock_team_image = 'https://scontent-atl3-2.xx.fbcdn.net/v/t31.18172-8/22769675_4721280142544_4790549516642822836_o.jpg?_nc_cat=100&ccb=1-7&_nc_sid=e3f864&_nc_ohc=n95GEGfHsRMAX-xE4Rm&_nc_ht=scontent-atl3-2.xx&oh=00_AfBd5TbXxGMqo47S21SQ5mXule_gUTTbTmTBEx72sTsw-w&oe=64208B0A'
UNASSIGNED = "unassigned"
# db = FireDB()


class TeamRef:
    teamId: str = None
    name: str = None
    sport: str = None
    status: str = None

    def __init__(self, team_obj={}):
        self.id = team_obj.get('id', str(uuid.uuid4()))
        self.teamId = team_obj.get('teamId', self.id)
        self.rosterId = team_obj.get('rosterId', "unassigned")
        self.tryoutId = team_obj.get('tryoutId', "unassigned")
        self.headCoachId = team_obj.get('headCoachId', UNASSIGNED)
        self.headCoachName = team_obj.get('headCoachName', "Unassigned")
        self.year = team_obj.get('year', "2023")
        self.ageGroup = team_obj.get('ageGroup', "U12")
        self.gender = team_obj.get('gender', 'female')
        self.name = team_obj.get('name', dg.generate_team_name())
        self.sport = team_obj.get('sport', "Soccer")
        self.status = team_obj.get('status', "active")
        self.imgUrl = team_obj.get('imgUrl', stock_team_image)

class Team:

    def __init__(self, team_obj={}, headCoachId:str="tnmjTR7r1HPwIaBb2oXrDrwXT842"):
        fakeName = dg.generate_full_name()
        self.id = team_obj.get('teamId', team_obj.get('id', str(uuid.uuid4())))
        self.headCoachId = team_obj.get('headCoachId', headCoachId)
        self.headCoachName = team_obj.get('headCoachName', team_obj.get('name', fakeName))
        self.coaches: [] = team_obj.get('coaches', [dg.generate_coach_user(userId=headCoachId)])
        self.managers: [] = team_obj.get('managers', [])
        self.organizations: [] = team_obj.get('organizations', [])
        self.rosterId = team_obj.get('roster', "9a9753e2-b886-11ed-a1e2-86f7c4c00ee1")
        self.tryoutId = team_obj.get('tryoutId', "")
        self.locationIds = team_obj.get('location', ["a9415342-b882-11ed-b197-86f7c4c00ee1"])
        self.season = team_obj.get('season', "Spring 2023")
        # self.schedule = team_obj.get('schedule', dg.generate_practice_schedule())
        self.name = team_obj.get('name', dg.generate_team_name())
        self.year = team_obj.get('year', dg.generate_team_year())
        self.ageGroup = team_obj.get('ageGroup', dg.generate_age_group())
        self.isActive = team_obj.get('isActive', True)
        self.gender = team_obj.get('gender', "female")
        self.imgUrl = team_obj.get('imgUrl', stock_team_image)
        self.sport = team_obj.get('sport', "soccer")
        self.hasReview = team_obj.get('hasReview', False)
        self.reviewIds = team_obj.get('reviewIds', None)
        self.dateCreated = team_obj.get('dateCreated', str(time.time()))
        self.dateUpdated = team_obj.get('dateUpdated', str(time.time()))
        self.type = team_obj.get('type', 'competitive')
        self.subType = team_obj.get('subType', 'youth')
        self.details = team_obj.get('details', 'Rag tag team of misfits')
        self.isFree = team_obj.get('isFree', False)
        self.status = team_obj.get('status', "open")
        self.mode = team_obj.get('mode', "tryouts")
        self.chatEnabled = team_obj.get('chatEnabled', False)

    def attachRoster(self, rosterId):
        self.rosterId = rosterId
    def attachTryout(self, tryoutId):
        self.tryoutId = tryoutId
    def attachHeadCoach(self, coachId):
        self.headCoachId = coachId

    # def saveToFirebase(self):
    #     self.updateUserRefsWithTeamRef()
    #     return db.add_object(self.id, self.__dict__, collection="teams")

    # def updateUserRefsWithTeamRef(self):
    #     teamRef = self.createTeamRef()
    #     from Models.Users.Coach import Coach
    #     for coach in self.coaches:
    #         co = db.get_object(collection="coaches", obj_id=coach['id'])
    #         oo = co[0][coach['id']]
    #         nc = Coach(oo)
    #         nc.teams.append(teamRef.__dict__)
    #         db.update_object(coach['id'], nc.__dict__, collection="coaches")

    def createTeamRef(self):
        return TeamRef(self.__dict__)

    # @classmethod
#     def makeAndSaveNewTeam(cls):
#         newTeam = cls()
#         newTeam.saveToFirebase()
#         return newTeam
#
#
# if __name__ == '__main__':
#     Team.makeAndSaveNewTeam()