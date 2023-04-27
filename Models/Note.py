import time
import uuid

from Firebase.FirebaseAdmin import FireDB
db = FireDB()
class Note:
    def __init__(self, obj={}):
        self.id = obj.get("id", str(uuid.uuid4()))
        self.ownerId = obj.get("ownerId", "tnmjTR7r1HPwIaBb2oXrDrwXT842")
        self.ownerName = obj.get("ownerName", "Chazz Romeo")
        self.dateCreated = obj.get("dateCreated", str(time.time()))
        self.dateUpdated = obj.get("dateUpdated", str(time.time()))
        self.coachId = obj.get("coachId", "tnmjTR7r1HPwIaBb2oXrDrwXT842")
        self.aboutTeamId = obj.get("aboutTeamId", "b17bcb69-0fd9-4df1-b61f-8e294f26a87e")
        self.aboutPlayerId = obj.get("aboutPlayerId", "a8d34f54-affa-11ed-a62e-86f7c4c00ee3")
        self.aboutCoachId = obj.get("aboutCoachId", "aboutcoachid")
        self.sport = obj.get("sport", "soccer")
        self.type = obj.get("type", "team")
        self.subtype = obj.get("subtype", "coach")
        self.message = obj.get("message", "I spoke with the captains about the issues and we are putting together a plan to address them.")

    def saveToFirebase(self):
        return db.add_object(self.id, self.__dict__, collection="notes")

    def createNote(self):
        #create a new note and return it
        self.saveToFirebase()

if __name__ == '__main__':
    note = Note()
    note.createNote()
