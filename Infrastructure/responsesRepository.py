from Infrastructure import responsesRepository
from domaine.Entities.responses import Response as ResponseEntity
from interface.models import Response as ResponseModel

class DjangoResponseRepository(responsesRepository):

    def _to_entity(self, r):
        return ResponseEntity(
            response_id=r.id,
            user_id=r.user_id,
            survey_id=r.survey_id,
            content=r.content,
            created_at=r.created_at
        )
        
        
    def get_by_id(self, response_id: int):
        try:
            r = ResponseModel.objects.get(id=response_id)
            return self._to_entity(r)
        except ResponseModel.DoesNotExist:
            return None


    def get_all(self):
        return [self._to_entity(r) for r in ResponseModel.objects.all()]


    def get_by_survey(self, survey_id: int):
        return [self._to_entity(r) for r in ResponseModel.objects.filter(survey_id=survey_id)]