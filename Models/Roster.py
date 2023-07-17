# from Firebase.FirebaseAdmin import FireDB
from Models.TestDataCreator.TestData import DataGeneration as dg
import uuid



class RosterRef:
    def __init__(self, json_obj={}):
        self.id = json_obj.get('id', str(uuid.uuid1()))
        self.rosterId = json_obj.get('rosterId', self.id)
        self.organizationId = json_obj.get('organizationId', "unassigned")
        self.coachId = json_obj.get('coachId', "unassigned")
        self.teamId = json_obj.get('teamId', "unassigned")

class Roster:
    def __init__(self, json_obj={}, playerCount=18):
        self.id = json_obj.get('id', str(uuid.uuid1()))
        self.teamId = json_obj.get('teamId', "250aaa4d-15f3-4948-a332-73507ab2ed1b")
        self.coachId = json_obj.get('coachId', "tnmjTR7r1HPwIaBb2oXrDrwXT842")
        self.organizationId = json_obj.get('organizationId', "unassigned")
        self.name = json_obj.get('name', "The Dumb Fuckery Bois 2022")
        self.season = json_obj.get('season', "2022/2023")
        self.year = json_obj.get('year', "2022")
        self.status = json_obj.get('status', "open")
        self.gender = json_obj.get('gender', 'female')
        self.sport = json_obj.get('sport', "Soccer")
        self.isLocked = json_obj.get('isLocked', False)
        self.players = json_obj.get('players', dg.generate_playerRefs(playerCount))

    def attachTeam(self, teamId):
        self.teamId = teamId

    def attachCoach(self, coachId):
        self.coachId = coachId

    # def saveToFirebase(self):
    #     db = FireDB("rosters")
    #     db.add_object(self.id, self.__dict__)

