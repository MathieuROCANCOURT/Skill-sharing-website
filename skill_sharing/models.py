from django.db import models


# Create your models here.


class Skill(models.Model):
    skill_name = models.TextField()
    Activity = models.ForeignKey(Activity, on_delete=models.CASCADE)


class Activity(models.Model):
    activity_name = models.TextField()
    details = models.TextField()


class User(models.Model):
    lastname = models.TextField()
    firstname = models.TextField()
    username = models.TextField()
    password = models.TextField()
    skills = models.ManyToManyRel(Skill)
