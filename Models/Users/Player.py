import time
import uuid


UNASSIGNED = "unassigned"

class PlayerRef:
    def __init__(self, json_obj={}):
        self.id = json_obj.get('id', str(uuid.uuid1()))
        self.name = json_obj.get('name', None)
        self.rank = json_obj.get('rank', None)
        self.tryoutTag = json_obj.get('tryoutTag', str(uuid.uuid1()))
        self.imgUrl = json_obj.get('imgUrl', "None")



class Player:
    def __init__(self, json_data):
        self.id = json_data.get("id", "")
        self.teamRef = json_data.get("teamRef", None)
        self.rank = json_data.get("rank", 0)
        self.number = json_data.get("number", 0)
        self.tryoutTag = json_data.get("tryoutTag", None)
        self.coachNotes: [] = json_data.get("coachNotes", [])
        self.age = json_data.get("age", 0)
        self.dob = json_data.get("dob", None)
        self.position = json_data.get("position", None)
        self.playerName = json_data.get("playerName", None)
        self.teamName = json_data.get("teamName", None)
        self.organizationRefs: [] = json_data.get("organizationRefs", [])
        self.teamIds = json_data.get("teamIds", [])
        self.hasReview = json_data.get("hasReview", False)
        self.reviewBundle = json_data.get("reviewBundle", None)
        self.dateCreated = json_data.get("dateCreated", time.time())
        self.dateUpdated = json_data.get("dateUpdated", time.time())
        self.name = json_data.get("name", None)
        self.firstName = json_data.get("firstName", None)
        self.lastName = json_data.get("lastName", None)
        self.type = json_data.get("type", None)
        self.subType = json_data.get("subType", None)
        self.details = json_data.get("details", None)
        self.isFree = json_data.get("isFree", False)
        self.status = json_data.get("status", None)
        self.mode = json_data.get("mode", None)
        self.imgUrl = json_data.get("imgUrl", None)
        self.sport = json_data.get("sport", None)
