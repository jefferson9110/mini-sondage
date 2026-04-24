from domaine.Entities.survey import Survey
from domaine.Interfaces.surveyRepository import IsurveyRepository
import Infrastructure.models


class surveyRepository(IsurveyRepository):
    def get_by_id(self, survey_id: int) -> Survey:
        # Implémentation pour récupérer un sondage par son ID
        try:
            survey=Infrastructure.models.surveyModel.objects.get(id=survey_id)
        except Infrastructure.models.surveyModel.DoesNotExist:
            raise ValueError(f"Survey avec l'ID {survey_id} introuvable.")
        return Survey(
            id=survey.id,
            title=survey.title,
            description=survey.description
        )
    
    def delete(self, survey_id: int) -> bool:
        try:
            Infrastructure.models.surveyModel.objects.get(id=survey_id).delete()
            return True
        except Infrastructure.models.surveyModel.DoesNotExist:
            return False