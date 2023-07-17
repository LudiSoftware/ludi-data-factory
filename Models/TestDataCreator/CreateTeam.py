from Models.Roster import Roster
from Models.Team import Team
from Models.TryOut import TryOut

from Firebase.FirebaseAdmin import FireDB
db = FireDB()

teamUUID = "b17bcb69-0fd9-4df1-b61f-8e294f26a87e"
coachUUID = "tnmjTR7r1HPwIaBb2oXrDrwXT842"

""" Roster """
def createRoster():
    roster = Roster()
    # roster.attachTeam(teamUUID)
    # roster.attachCoach(coachUUID)
    return roster

def saveRoster(roster):
    return db.add_object(roster.id, roster.__dict__, collection="rosters")

""" TryOut """
def createTryOut():
    # tRoster = createRoster()
    # saveRoster(tRoster)
    tryOut = TryOut()
    tryOut.attachTeam(teamUUID)
    tryOut.attachCoach(coachUUID)
    return tryOut

def saveTryOut(tryOut):
    return db.add_object(tryOut.id, tryOut.__dict__, collection="tryouts")

""" Team """
def createTeam(rosterId, tryOutId):
    team = Team()
    team.attachHeadCoach(coachUUID)
    team.attachRoster(rosterId)
    team.attachTryout(tryOutId)
    return team

def saveTeam(team):
    return db.add_object(team.id, team.__dict__, collection="teams")

if __name__ == "__main__":
    # Roster
    # roster = createRoster()
    # rosterId = saveRoster(roster)
    # TryOut
    tryOut = createTryOut()
    tryOutId = saveTryOut(tryOut)
    # Team
    # team = createTeam("rosterId", "tryOutId")
    # teamId = saveTeam(team)