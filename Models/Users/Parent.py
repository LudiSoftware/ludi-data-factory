
import time
UNASSIGNED = "unassigned"



class ParentRef:
    def __init__(self, parent_ref_dict=None):
        self.parentId = parent_ref_dict.get('parentId') if parent_ref_dict else None
        self.name = parent_ref_dict.get('name') if parent_ref_dict else None
        # self.playerRefs = [PlayerRef(player_ref_dict) for player_ref_dict in parent_ref_dict.get('playerRefs', [])] if parent_ref_dict else None
        # self.teamRefs = [TeamRef(team_ref_dict) for team_ref_dict in parent_ref_dict.get('teamRefs', [])] if parent_ref_dict else None
        # self.organizationRefs = [OrganizationRef(org_ref_dict) for org_ref_dict in parent_ref_dict.get('organizationRefs', [])] if parent_ref_dict else None

class Parent:
    def __init__(self, json_data):
        self.id = json_data.get("id", "")
        self.player = json_data.get("player", False)
        self.playerRefs = json_data.get("playerRefs", None)
        self.team = json_data.get("team", False)
        self.teamRefs = json_data.get("teamRefs", None)
        self.organizationRefs = json_data.get("organizationRefs", None)
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

