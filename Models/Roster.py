
import uuid



class CoachRosters:
    def __init__(self, json_obj={}):
        self.id = json_obj.get('id', str(uuid.uuid1()))
        self.coachId = json_obj.get('coachId', self.id)
        self.rosters = json_obj.get('rosters', [])


class Roster:
    def __init__(self, json_obj={}):
        self.id = json_obj.get('id', str(uuid.uuid1()))
        self.name = json_obj.get('name', "Roster Name")
        self.season = json_obj.get('season', "2023/2024")
        self.gender = json_obj.get('gender', 'female')
        self.isLocked = json_obj.get('isLocked', False)
        self.teamId = json_obj.get('teamId', self.id)
        self.players = json_obj.get('players', [])