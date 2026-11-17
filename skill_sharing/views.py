from django.contrib.auth import logout
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods


# Create your views here.

@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the skill_sharing index.")


@require_http_methods(["GET"])
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("polls:login"))
