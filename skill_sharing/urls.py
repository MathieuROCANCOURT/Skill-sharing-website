from django.urls import path

from . import views

app_name = "skill_sharing"
urlpatterns = [
    path("", views.index, name="index"),
]
