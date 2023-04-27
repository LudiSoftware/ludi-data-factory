import uuid
import time
# from Firebase.FirebaseAdmin import FireDB
from Models.TestDataCreator.TestData import DataGeneration as dg
dg = dg()
# db = FireDB()
class TryOut:
    def __init__(self, tryout_obj={}, headCoachId="tnmjTR7r1HPwIaBb2oXrDrwXT842", rosterId="59d0b9ca-cdfd-11ed-8ff9-86f7c4c00ee2"):
        self.id = tryout_obj.get('id', str(uuid.uuid4()))
        # From Team (5)
        self.isActive = tryout_obj.get('isActive', True)
        self.isFinalized = tryout_obj.get('isFinalized', False)
        self.teamId = tryout_obj.get('teamId', "b17bcb69-0fd9-4df1-b61f-8e294f26a87e")
        self.headCoachId = tryout_obj.get('headCoachId', headCoachId)
        self.headCoachName = tryout_obj.get('headCoachName', "Chazz Romeo")
        # References (3)
        self.coachIds = tryout_obj.get('coachIds', [dg.generate_coachRef(userId=headCoachId)])
        self.managerIds = tryout_obj.get('managerIds', [])
        self.organizationIds = tryout_obj.get('organizationIds', [])
        # Rosters (1)
        self.rosterId = tryout_obj.get('rosterId', rosterId)
        # Schedule (1)
        # self.schedule = tryout_obj.get('schedule', dg.generate_tryout_schedule())
        # Team Attributes (3)
        self.year = tryout_obj.get('year', dg.generate_team_year())
        self.ageGroup = tryout_obj.get('ageGroup', dg.generate_age_group())
        self.gender = tryout_obj.get('gender', "female")
        #base (12)
        self.dateCreated = tryout_obj.get('dateCreated', str(time.time()))
        self.dateUpdated = tryout_obj.get('dateUpdated', str(time.time()))
        self.name = tryout_obj.get('name', "Tryouts: Fall2023/Spring2024")
        self.type = tryout_obj.get('type', "competitive")
        self.subType = tryout_obj.get('subType', "youth")
        self.details = tryout_obj.get('details', "This is a no joke tryout joel!")
        self.isFree = tryout_obj.get('isFree', False)
        self.status = tryout_obj.get('status', "open")
        self.mode = tryout_obj.get('mode', "edit")
        self.imgUrl = tryout_obj.get('imgUrl', "")
        self.sport = tryout_obj.get('sport', "soccer")
        self.chatEnabled = tryout_obj.get('chatEnabled', True)

    def attachTeam(self, teamId):
        self.teamId = teamId

    def attachCoach(self, coachId):
        self.headCoachId = coachId

    # def saveToFirebase(self):
    #     return db.add_object(self.id, self.__dict__, collection="tryouts")

    # @classmethod
#     def makeAndSaveNewTeam(cls):
#         newTryout = cls()
#         newTryout.saveToFirebase()
#         return newTryout
#
# if __name__ == '__main__':
#     newTryout = TryOut.makeAndSaveNewTeam()