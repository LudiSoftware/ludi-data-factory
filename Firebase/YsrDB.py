from Models.Users.Coach import Coach
from Models.Users.Parent import Parent
from Models.Users.Player import Player
from Models.Users.User import User
from Firebase.FirebaseAdmin import FireDB

class UserManager:

    def __init__(self):
        self.db = FireDB()

    def get_user_by_id(self, user_id, toUser=False):
        json_user = self.db.get_object(user_id, collection="users")[0][user_id]
        if not toUser:
            return json_user
        return User(firebase_user=json_user)

    def parse_user_to(self, user_obj, parse_to, save=False):
        if parse_to == "coach":
            new_user = Coach(firebase_user=user_obj)
        elif parse_to == "parent":
            new_user = Parent(firebase_user=user_obj)
        elif parse_to == "player":
            new_user = Player(firebase_user=user_obj)
        else:
            return None

        if save:
            id = new_user.ownerId
            if parse_to == "coach":
                user_obj["coach"] = True
                save_to = "coaches"
            elif parse_to == "parent":
                user_obj["parent"] = True
                save_to = "parents"
            elif parse_to == "player":
                user_obj["player"] = True
                save_to = "players"

            self.update_base_user_to_firebase(id, user_obj)
            self.save_promoted_user_to_firebase(id, new_user, save_to)
        return new_user

    def save_promoted_user_to_firebase(self, user_id, user_obj, save_to):
        if type(user_obj) not in [dict]:
            user_obj = user_obj.__dict__
        return self.db.add_object(user_id, user_obj, collection=save_to)

    def update_base_user_to_firebase(self, user_id, user_obj):
        return self.db.update_object(user_id, user_obj, collection="users")

    def promote_user(self, user_id, promote_to, save_to_firebase=True):
        user = self.get_user_by_id(user_id, toUser=True)
        return self.parse_user_to(user, parse_to=promote_to, save=save_to_firebase)