from django.urls import path
from .views import ResponseParIdView, ToutesLesResponsesView, ResponseParSurveyView

urlpatterns = [
    path('responses/', ToutesLesResponsesView.as_view()),
    path('responses/<int:response_id>/', ResponseParIdView.as_view()),
    path('surveys/<int:survey_id>/responses/', ResponseParSurveyView.as_view()),
]