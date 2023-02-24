import time
import uuid

from Firebase.FirebaseAdmin import FireDB
db = FireDB()
class Note:
    def __init__(self, obj={}):
        self.id = obj.get("id", str(uuid.uuid4()))
        self.ownerId = obj.get("id", "tnmjTR7r1HPwIaBb2oXrDrwXT842")
        self.ownerName = obj.get("ownerName", "David Cox")
        self.dateCreated = obj.get("dateCreated", str(time.time()))
        self.dateUpdated = obj.get("dateUpdated", str(time.time()))
        self.coachId = obj.get("coachId", "tnmjTR7r1HPwIaBb2oXrDrwXT842")
        self.aboutTeamId = obj.get("aboutTeamId", "aboutteamid")
        self.aboutPlayerId = obj.get("aboutPlayerId", "a8d34f54-affa-11ed-a62e-86f7c4c00ee3")
        self.message = obj.get("message", "His through ball during the 3rd scrimmage, unbelievable!")

    def saveToFirebase(self):
        return db.add_object_by_user_id(self.ownerId, self.id, self.__dict__, collection="notes")

    def createNote(self):
        #create a new note and return it
        self.saveToFirebase()

if __name__ == '__main__':
    note = Note()
    note.createNote()
