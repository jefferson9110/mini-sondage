from django.db import models

#On ne crée pas ne table user car django le fait deja pour nous par l'imporation du 2e package

from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Response(models.Model):
    choix = [('OUI', 'Oui'), ('NON', 'Non')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    content = models.CharField(max_length=3, choices=choix)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'survey')  # Empêche un double vote

    def __str__(self):
        return f"{self.user.username} -> {self.survey.title}"
    