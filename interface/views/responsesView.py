from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from application.useCase.responsesUseCase import ResponseParIdUseCase, Response
ParSurveyUseCase, ResponseParSurveyUseCase
from Infrastructure.responsesRepository import DjangoResponseRepository
from .serializers import ReponseOutputSerializer



class ResponseParIdView(APIView):
    def get(self, request, response_id):
        try:
            r = ResponseParIdUseCase(DjangoResponseRepository()).execute(response_id)
        except ValueError as e:
            return DRFResponse({"erreur": str(e)}, status=status.HTTP_404_NOT_FOUND)
        return DRFResponse(ResponseOutputSerializer(r).data, status=status.HTTP_200_OK)


class ToutesLesResponsesView(APIView):
    def get(self, request):
        responses = ResponseParSurveyUseCase(DjangoResponseRepository()).execute()
        return DRFResponse(ResponseOutputSerializer(responses, many=True).data, status=status.HTTP_200_OK)



class ResponseParSurveyView(APIView):
    def get(self, request, survey_id):
        try:
            responses = ResponseParSurveyUseCase(DjangoResponseRepository()).execute(survey_id)
        except ValueError as e:
            return DRFResponse({"erreur": str(e)}, status=status.HTTP_404_NOT_FOUND)
        return DRFResponse(ResponseOutputSerializer(responses, many=True).data, status=status.HTTP_200_OK)