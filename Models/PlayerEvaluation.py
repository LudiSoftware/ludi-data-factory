import uuid


class PlayerEvaluationRef:
    def __init__(self, eval_obj=None):
        self.evalId = eval_obj.get('evalId', str(uuid.uuid1()))
        self.coachId = eval_obj.get('coachId', None)
        self.playerId = eval_obj.get('playerId', None)
        self.teamId = eval_obj.get('teamId', None)

class PlayerEvaluation:
    def __init__(self, eval_obj=None):
        self.id = eval_obj.get('id', str(uuid.uuid1()))
        self.coachId = eval_obj.get('coachId', None)
        self.playerId = eval_obj.get('playerId', None)
        self.teamId = eval_obj.get('teamId', None)
        self.overall_score = eval_obj.get('overall_score', 0)
        self.notes = eval_obj.get('notes', [])
        self.attributes = eval_obj.get('attributes', [])
        self.technical_skills = eval_obj.get('technical_skills', "technical skills")
        self.technical_skills_score = eval_obj.get('technical_skills_score', 0)
        self.physical_fitness = eval_obj.get('physical_fitness', "physical fitness")
        self.physical_fitness_score = eval_obj.get('physical_fitness_score', 0)
        self.tactical_understanding = eval_obj.get('tactical_understanding', "tactical understanding")
        self.tactical_understanding_score = eval_obj.get('tactical_understanding_score', 0)
        self.attitude = eval_obj.get('attitude', "attitude")
        self.attitude_score = eval_obj.get('attitude_score', 0)
        self.decision_making = eval_obj.get('decision_making', "decision making")
        self.decision_making_score = eval_obj.get('decision_making_score', 0)
        self.communication = eval_obj.get('communication', "communication")
        self.communication_score = eval_obj.get('communication_score', 0)
        self.teamwork = eval_obj.get('teamwork', "teamwork")
        self.teamwork_score = eval_obj.get('teamwork_score', 0)
        self.coachability = eval_obj.get('coachability', "coachability")
        self.coachability_score = eval_obj.get('coachability_score', 0)
        self.versatility = eval_obj.get('versatility', "versatility")
        self.versatility_score = eval_obj.get('versatility_score', 0)
        self.dateCreated = tryout_obj.get('dateCreated', time.time())





