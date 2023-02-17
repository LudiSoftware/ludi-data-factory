

class Note:
    def __init__(self, obj=None):
        self.id = obj.get("id", None)
        self.ownerId = obj.get("id", None)
        self.dateCreated = obj.get("dateCreated", None)
        self.dateUpdated = obj.get("dateUpdated", None)
        self.coachId = obj.get("coachId", None)
        self.aboutTeamId = obj.get("aboutTeamId", None)
        self.aboutPlayerId = obj.get("aboutPlayerId", None)
        self.message = obj.get("message", None)