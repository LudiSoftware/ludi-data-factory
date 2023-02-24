import uuid
import time
from Models.TestDataCreator.TestData import DataGeneration as dg
dg = dg()
class TryOut:
    def __init__(self, tryout_obj=None, headCoachId=None):
        self.id = tryout_obj.get('id', str(uuid.uuid4()))
        # From Team
        self.teamId = tryout_obj.get('teamId', tryout_obj.get('id', str(uuid.uuid4())))
        self.headCoachId = tryout_obj.get('headCoachId', headCoachId)
        self.headCoachName = tryout_obj.get('headCoachName', dg.generate_full_name())
        self.coaches = tryout_obj.get('coaches', [dg.generate_coachRef(userId=headCoachId)])
        self.managers = tryout_obj.get('managers', [])
        self.organizations = tryout_obj.get('organizations', [])
        self.year = tryout_obj.get('year', dg.generate_team_year())
        # New
        self.notes = tryout_obj.get('notes', [])
        self.tryoutRoster = tryout_obj.get('tryoutRoster', dg.generate_roster(20))
        self.coachRosters = tryout_obj.get('coachRosters', [])
        self.schedule = tryout_obj.get('schedule', dg.generate_tryout_schedule())
        self.ageGroup = tryout_obj.get('ageGroup', dg.generate_age_group())
        self.isActive = tryout_obj.get('isActive', True)
        self.gender = tryout_obj.get('gender', "female")
        #base
        self.dateCreated = tryout_obj.get('dateCreated', str(time.time()))
        self.dateUpdated = tryout_obj.get('dateUpdated', str(time.time()))
        self.name = tryout_obj.get('name', "Tryouts: Fall2023/Spring2024")
        self.type = tryout_obj.get('type', "competitive")
        self.subType = tryout_obj.get('subType', "youth")
        self.details = tryout_obj.get('details', "This is a no joke tryout!")
        self.isFree = tryout_obj.get('isFree', False)
        self.status = tryout_obj.get('status', "open")
        self.mode = tryout_obj.get('mode', "edit")
        self.imgUrl = tryout_obj.get('imgUrl', "")
        self.sport = tryout_obj.get('sport', "soccer")
        self.chatEnabled = tryout_obj.get('chatEnabled', True)

# create a function that creates a new TryOut object and fills it with mock data
def create_mock_tryout():
    # create a new TryOut object
    tryout = TryOut()
    # set the name of the TryOut object
    tryout.name = "Mock TryOut"
    tryout.teamId = "Mock Team Id"
    tryout.notes = "Mock Notes"
    tryout.tryoutRoster = "Mock Players Registered Refs"
    tryout.coachRosters = "Mock Players Ranked Refs"
    tryout.headCoachId = "Mock Head Coach Id"
    tryout.headCoachName = "Mock Head Coach Name"
    tryout.coaches = []
    tryout.managers = "Mock Manager Refs"
    tryout.organizations = "Mock Organization Refs"
    tryout.schedule = "Mock Schedule"
    tryout.year = "Mock Year"
    tryout.ageGroup = "Mock Age Group"
    tryout.isActive = "Mock Is Active"
    # return the TryOut object
    return tryout