import uuid

class Evaluation:
    def __init__(self, eval_obj=None):
        self.id = eval_obj.get('id', str(uuid.uuid1()))
        self.coachId = eval_obj.get('coachId', None)
        self.playerId = eval_obj.get('playerId', None)
        self.teamId = eval_obj.get('teamId', None)
        self.overall_score = eval_obj.get('overall_score', None)
        self.coachNotes = eval_obj.get('coachNotes', None)
        self.technical_skills = eval_obj.get('technical_skills', None)
        self.technical_skills_score = eval_obj.get('technical_skills_score', None)
        self.physical_fitness = eval_obj.get('physical_fitness', None)
        self.physical_fitness_score = eval_obj.get('physical_fitness_score', None)
        self.tactical_understanding = eval_obj.get('tactical_understanding', None)
        self.tactical_understanding_score = eval_obj.get('tactical_understanding_score', None)
        self.attitude = eval_obj.get('attitude', None)
        self.attitude_score = eval_obj.get('attitude_score', None)
        self.decision_making = eval_obj.get('decision_making', None)
        self.decision_making_score = eval_obj.get('decision_making_score', None)
        self.communication = eval_obj.get('communication', None)
        self.communication_score = eval_obj.get('communication_score', None)
        self.teamwork = eval_obj.get('teamwork', None)
        self.teamwork_score = eval_obj.get('teamwork_score', None)
        self.coachability = eval_obj.get('coachability', None)
        self.coachability_score = eval_obj.get('coachability_score', None)
        self.versatility = eval_obj.get('versatility', None)
        self.versatility_score = eval_obj.get('versatility_score', None)





