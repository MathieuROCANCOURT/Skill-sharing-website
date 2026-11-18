from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    skill_name = models.TextField()
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Activity(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    activity_name = models.TextField()
    details = models.TextField(blank=True)


class Calendar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Slot(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    attend = models.BooleanField(default=False)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None, on_delete=models.CASCADE)
