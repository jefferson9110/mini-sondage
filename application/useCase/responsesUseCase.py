class ResponseParIdUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, response_id: int):
        response = self.repo.get_by_id(response_id)
        if not response:
            raise ValueError(f"Aucune response avec l'id {response_id}")
        return response

class ToutesLesResponsesUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self):
        return self.repo.get_all()


class ResponseParSurveyUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, survey_id: int):
        responses = self.repo.get_by_survey(survey_id)
        if not responses:
            raise ValueError(f"Aucune response pour le sondage {survey_id}")
        return responses