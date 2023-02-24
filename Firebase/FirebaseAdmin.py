import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from F import OS

cwd = OS.get_path(__file__)

class FireDB:
    collection = ""

    def __init__(self, collection:str=None):
        cred = credentials.Certificate(f"{cwd}/usysr.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://usysr-a16ef-default-rtdb.firebaseio.com'
        })
        self.REF = db.reference('/')
        self.collection = collection

    # Add an object to the database
    def add_object(self, obj_id:str, obj:{}, collection=None):
        return self.REF.child(self.collection if not collection else collection).child(obj_id).set(obj)

    def add_object_by_user_id(self, user_id:str, obj_id:str, obj:{}, collection=None):
        return self.REF.child(self.collection if not collection else collection).child(user_id).child(obj_id).set(obj)

    # Update an object in the database
    def update_object(self, obj_id, obj, collection=None):
        return self.REF.child(self.collection if not collection else collection).child(obj_id).update(obj)

    # Remove an object from the database
    def remove_object(self, obj_id, collection=None):
        ref = self.REF.child(self.collection if not collection else collection).child(obj_id)
        return ref.delete()

    def get_object(self, obj_id, collection=None):
        return self.REF.child(self.collection if not collection else collection).get(obj_id)


if __name__ == '__main__':
    # from Models.Team import Team
    # newTeam = Team()
    # newTeam.name = "3 PyCharm United"
    # see = newTeam.__dict__
    # print(see)
    db = FireDB("teams")
    print(db.get_object("4f6b1846-a9d0-11ed-ab87-86f7c4c00ee3"))
