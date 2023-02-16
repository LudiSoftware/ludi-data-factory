from Firebase.FirebaseAdmin import FireDB


db = FireDB()

def get_user_by_id(user_id, toUser=False):
    json_user = db.get_object(user_id, collection="users")[0][user_id]
    if not toUser:
        return json_user
    from Models.Users.User import User
    newUser = User(firebase_user=json_user)
    return newUser

def parseUserTo(userObj:{}, parseTo:str, save=False):
    if parseTo == "coach":
        from Models.Users.Coach import Coach
        newCoach = Coach(firebase_user=userObj)
        if save:
            id = newCoach.ownerId
            userObj.coach = True
            updateBaseUserToFirebase(id, userObj)
            savePromotedUserToFirebase(id, newCoach, parseTo)
        return newCoach
    elif parseTo == "parent":
        from Models.Users.Parent import Parent
        newParent = Parent(firebase_user=userObj)
        if save:
            id = newParent.ownerId
            userObj.parent = True
            updateBaseUserToFirebase(id, userObj)
            savePromotedUserToFirebase(id, newParent, parseTo)
        return newParent
    elif parseTo == "player":
        from Models.Users.Player import Player
        newPlayer = Player(firebase_user=userObj)
        if save:
            id = newPlayer.ownerId
            userObj.player = True
            updateBaseUserToFirebase(id, userObj)
            savePromotedUserToFirebase(id, newPlayer, parseTo)
        return newPlayer

def savePromotedUserToFirebase(userId:str, userObj:{}, saveTo:str):
    if type(userObj) not in [dict]:
        userObj = userObj.__dict__
    if saveTo == "coach":
        return db.add_object(userId, userObj, collection="coaches")
    elif saveTo == "parent":
        return db.add_object(userId, userObj, collection="parents")
    elif saveTo == "player":
        return db.add_object(userId, userObj, collection="players")

def updateBaseUserToFirebase(userId:str, userObj:{}):
    return db.update_object(userId, userObj.__dict__, collection="users")

def promote_user(userId:str, promoteTo:str, saveToFirebase=True):
    """ Main Promote User Function """
    user = get_user_by_id(userId, toUser=True)
    return parseUserTo(user, parseTo=promoteTo, save=saveToFirebase)

if __name__ == '__main__':
    promotion = "coach"
    userID = "tnmjTR7r1HPwIaBb2oXrDrwXT842"
    promote_user(userID, promotion, saveToFirebase=True)


