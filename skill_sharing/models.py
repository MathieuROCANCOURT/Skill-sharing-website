from django.conf import settings
from django.db import models


class Skill(models.Model):
    skill_name = models.TextField()
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    @staticmethod
    def get_all_skills():
        return Skill.objects.all()


class Activity(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    activity_name = models.TextField()

    def __str__(self):
        return self.activity_name

    @staticmethod
    def only_activities_user(user):
        activities = Activity.objects.filter(skill__user__id=user.id)
        return activities


class Calendar(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Slot(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    attend = models.BooleanField(default=False)
    details = models.TextField(blank=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        date_format = '%m/%d/%Y'

        if self.start_date == self.end_date:
            display_slot = "{0} le {1} avec {2} {3}".format(self.activity.activity_name,
                                                            self.start_date.strftime(date_format),
                                                            self.calendar.user.first_name,
                                                            self.calendar.user.last_name)
        else:
            display_slot = "{0} du {1} au {2} avec {3} {4}".format(self.activity.activity_name,
                                                                   self.start_date.strftime(date_format),
                                                                   self.end_date.strftime(date_format),
                                                                   self.calendar.user.first_name,
                                                                   self.calendar.user.last_name)

        if self.details != "":
            display_slot += ", " + self.details
        return display_slot

    @staticmethod
    def add_slot(start_date, end_date, activity, calendar, details):
        slot = Slot(start_date=start_date, end_date=end_date, activity=activity, calendar=calendar, details=details)
        slot.save()

    @staticmethod
    def remove_slot(slot):
        if Slot.objects.filter(slot=slot).exists():
            Slot.objects.filter(slot=slot).delete()
