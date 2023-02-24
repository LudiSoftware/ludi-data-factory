
import uuid



class CoachRoster:
    def __init__(self, json_obj={}):
        self.coachId = json_obj.get('coachId', "")
        self.rosters = json_obj.get('rosters', [])


class Roster:
    def __init__(self, json_obj={}):
        self.id = json_obj.get('id', str(uuid.uuid1()))
        self.players = json_obj.get('players', [])