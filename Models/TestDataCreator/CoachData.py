from Models.TestDataCreator.TestData import DataGeneration


class CoachDG:
    @staticmethod
    def generate_coach_roster(coachId, roster):
        from Models.Roster import RosterRef
        item = {"coachId": coachId, "rosters": [roster]}
        coachRoster = RosterRef(item)
        return coachRoster.__dict__

    @staticmethod
    def generate_coach_refs(num_players: int = 1) -> [dict]:
        coach_refs = []
        for i in range(num_players):
            newCoachRef = DataGeneration.generate_coachRef()
            coach_refs.append(newCoachRef.__dict__)
        return coach_refs