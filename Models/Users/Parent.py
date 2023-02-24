import uuid
import time
UNASSIGNED = "unassigned"



class ParentRef:
    def __init__(self, parent_ref_dict=None):
        self.parentId = parent_ref_dict.get('parentId') if parent_ref_dict else None
        self.id = parent_ref_dict.get('id', str(uuid.uuid4()))
        self.name = parent_ref_dict.get('name') if parent_ref_dict else None
        self.isManager = parent_ref_dict.get('isManager', False)
        self.players = parent_ref_dict.get('players', [])
        self.teams = parent_ref_dict.get('teams', [])
        self.organizations = parent_ref_dict.get('organizations', [])

class Parent:
    def __init__(self, json_data):
        self.id = json_data.get("id", "")
        self.hasPlayer = json_data.get("hasPlayer", False)
        self.players = json_data.get("playerRefs", None)
        self.team = json_data.get("team", False)
        self.teams = json_data.get("teams", None)
        self.organizations = json_data.get("organizations", None)
        #Base
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

