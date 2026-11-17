from django.conf import settings
from django.db import models

from django.contrib.auth.models import User


class Skill(models.Model):
    skill_name = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Activity(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    activity_name = models.TextField()
    details = models.TextField(blank=True)


class Calendar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Slot(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    attend = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
