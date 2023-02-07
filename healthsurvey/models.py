
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feeling = models.CharField(max_length=100)
    stress = models.IntegerField()
    coping_mechanisms = models.TextField()
    date_taken = models.DateTimeField(auto_now_add=True)

