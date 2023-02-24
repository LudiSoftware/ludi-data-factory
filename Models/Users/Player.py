import time
import uuid


from Models.TestDataCreator.TestData import DataGeneration as dg
dg = dg()

UNASSIGNED = "unassigned"

class PlayerRef:
    def __init__(self, user_or_player_json={}):
        self.id = user_or_player_json.get('id', str(uuid.uuid1()))
        self.playerId = user_or_player_json.get('playerId', str(uuid.uuid1()))
        self.name = user_or_player_json.get('name', dg.generate_full_name())
        self.rank = user_or_player_json.get('rank', dg.generate_player_rank())
        self.number = user_or_player_json.get('number', dg.generate_number())
        self.position = user_or_player_json.get('position', dg.generate_position())
        self.foot = user_or_player_json.get('foot', dg.generate_foot())
        self.dob = user_or_player_json.get('dob', dg.generate_birthday())
        self.tryoutTag = user_or_player_json.get('tryoutTag', dg.generate_tryout_tag())
        self.imgUrl = user_or_player_json.get('imgUrl', dg.generate_player_img_url())
        self.pointX = user_or_player_json.get('pointX', 0)
        self.pointY = user_or_player_json.get('pointY', 0)


class Player:
    def __init__(self, user_or_playerRef_json=None):
        self.id = user_or_playerRef_json.get("id", uuid.uuid4())
        self.team = user_or_playerRef_json.get("team", None)
        self.rank = user_or_playerRef_json.get("rank", 0)
        self.number = user_or_playerRef_json.get("number", 0)
        self.tryoutTag = user_or_playerRef_json.get("tryoutTag", None)
        self.notes: [] = user_or_playerRef_json.get("notes", [])
        self.evaluations = user_or_playerRef_json.get('evaluations', None)
        self.age = user_or_playerRef_json.get("age", "16")
        self.dob = user_or_playerRef_json.get("dob", "11/29/07")
        self.position = user_or_playerRef_json.get("position", "forward")
        self.foot = user_or_playerRef_json.get("foot", "right")
        self.teamName = user_or_playerRef_json.get("teamName", None)
        self.playerName = user_or_playerRef_json.get("playerName", None)
        self.organizations: [] = user_or_playerRef_json.get("organizations", [])
        self.teams = user_or_playerRef_json.get("teams", [])
        self.contacts = user_or_playerRef_json.get("contacts", [])
        self.hasReview = user_or_playerRef_json.get("hasReview", False)
        self.reviewBundle = user_or_playerRef_json.get("reviewBundle", None)
        #base
        self.dateCreated = user_or_playerRef_json.get("dateCreated", str(time.time()))
        self.dateUpdated = user_or_playerRef_json.get("dateUpdated", str(time.time()))
        self.name = user_or_playerRef_json.get("name", None)
        self.firstName = user_or_playerRef_json.get("firstName", None)
        self.lastName = user_or_playerRef_json.get("lastName", None)
        self.type = user_or_playerRef_json.get("type", None)
        self.subType = user_or_playerRef_json.get("subType", None)
        self.details = user_or_playerRef_json.get("details", None)
        self.isFree = user_or_playerRef_json.get("isFree", False)
        self.status = user_or_playerRef_json.get("status", None)
        self.mode = user_or_playerRef_json.get("mode", None)
        self.imgUrl = user_or_playerRef_json.get("imgUrl", None)
        self.sport = user_or_playerRef_json.get("sport", None)

