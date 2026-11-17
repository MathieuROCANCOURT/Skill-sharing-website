from django.conf import settings
from django.db import models


# Create your models here.


class Skill(models.Model):
    skill_name = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Activity(models.Model):
    Activity = models.ForeignKey(Skill, on_delete=models.CASCADE)
    activity_name = models.TextField()
    details = models.TextField()
