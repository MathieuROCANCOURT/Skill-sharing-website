from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import View

from . import views

app_name = "skill_sharing"
urlpatterns = [
    # ex: /skill_sharing
    path("", views.index, name="index"),
    # ex: /skill_sharing/login
    path("login/",
         auth_views.LoginView.as_view(template_name="skill_sharing/login.html", next_page="/skill_sharing/home/"),
         name="login"),
    # ex: /skill_sharing/logout
    path("logout/", views.logout_view, name="logout"),
    # ex: /skill_sharing/home
    path("home/", views.home, name="home"),
    # ex: /skill_sharing/home
    path("home/add_skill", views.add_skill, name="add_skill"),
]
