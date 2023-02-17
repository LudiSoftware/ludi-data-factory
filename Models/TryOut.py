import uuid
import time

class TryOut:
    def __init__(self, tryout_obj=None):
        self.id = str(uuid.uuid4())
        self.teamId = tryout_obj.get('teamId', None)
        self.notes = tryout_obj.get('notes', None)
        self.playersRegisteredRefs = tryout_obj.get('playersRegisteredRefs', None)
        self.playersRankedRefs = tryout_obj.get('playersRankedRefs', None)
        self.headCoachId = tryout_obj.get('headCoachId', None)
        self.headCoachName = tryout_obj.get('headCoachName', None)
        self.coachRefs = tryout_obj.get('coachRefs', None)
        self.managerRefs = tryout_obj.get('managerRefs', None)
        self.organizationRefs = tryout_obj.get('organizationRefs', None)
        self.schedule = tryout_obj.get('schedule', None)
        self.year = tryout_obj.get('year', None)
        self.ageGroup = tryout_obj.get('ageGroup', None)
        self.isActive = tryout_obj.get('isActive', None)
        self.gender = tryout_obj.get('gender', None)
        self.dateCreated = tryout_obj.get('dateCreated', time.time())
        self.dateUpdated = tryout_obj.get('dateUpdated', time.time())
        self.name = tryout_obj.get('name', None)
        self.firstName = tryout_obj.get('firstName', None)
        self.lastName = tryout_obj.get('lastName', None)
        self.type = tryout_obj.get('type', None)
        self.subType = tryout_obj.get('subType', None)
        self.details = tryout_obj.get('details', None)
        self.isFree = tryout_obj.get('isFree', False)
        self.status = tryout_obj.get('status', None)
        self.mode = tryout_obj.get('mode', None)
        self.imgUrl = tryout_obj.get('imgUrl', None)
        self.sport = tryout_obj.get('sport', None)
        self.chatEnabled = tryout_obj.get('chatEnabled', False)

# create a function that creates a new TryOut object and fills it with mock data
def create_mock_tryout():
    # create a new TryOut object
    tryout = TryOut()
    # set the name of the TryOut object
    tryout.name = "Mock TryOut"
    tryout.teamId = "Mock Team Id"
    tryout.notes = "Mock Notes"
    tryout.playersRegisteredRefs = "Mock Players Registered Refs"
    tryout.playersRankedRefs = "Mock Players Ranked Refs"
    tryout.headCoachId = "Mock Head Coach Id"
    tryout.headCoachName = "Mock Head Coach Name"
    tryout.coachRefs = [CoachRef]
    tryout.managerRefs = "Mock Manager Refs"
    tryout.organizationRefs = "Mock Organization Refs"
    tryout.schedule = "Mock Schedule"
    tryout.year = "Mock Year"
    tryout.ageGroup = "Mock Age Group"
    tryout.isActive = "Mock Is Active"
    # return the TryOut object
    return tryout