from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .models import Skill


# Create your views here.

@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the skill_sharing index.")


@require_http_methods(["GET"])
@login_required(login_url="/skill_sharing/login/")
def home(request):
    return render(request, 'skill_sharing/home.html', {'skills': Skill.objects.all().filter(user_id=request.user.id)})


@require_http_methods(["GET"])
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("skill_sharing:login"))
