from domaine.Entities.survey import Survey
from Infrastructure.surveyRepository import surveyRepository

class surveyUseCase:
    def __init__(self, survey:Isurvey):
        self.survey = survey
        def execute(self, survey_id: int) -> Survey:
            return self.survey.get_by_id(survey_id)
        

    