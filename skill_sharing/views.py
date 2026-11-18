from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .models import Skill, Activity, Slot, Calendar
from .skill import SkillAddForm


# Create your views here.

@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the skill_sharing index.")


@require_http_methods(["GET"])
@login_required(login_url="/skill_sharing/login/")
def home(request):
    skills = [skill.skill_name for skill in Skill.objects.filter(user__id=request.user.id)]
    slots = [slot for slot in Slot.objects.all() if slot.user is not None and slot.calendar.user_id == request.user.id]
    slots_receive = [slot for slot in Slot.objects.all() if slot.user is not None and slot.user.id == request.user.id]
    slots_available = [slot for slot in Slot.objects.all() if
                       slot.calendar.user_id == request.user.id and slot.user is None]

    # Add the slots received by the others users in the site and reverse the help directory
    for slots_receive_slot in slots_receive:
        slots_receive_slot.attend = ~slots_receive_slot.attend
        slots_receive_slot.user = slots_receive_slot.calendar.user

    return render(request, 'skill_sharing/home.html',
                  {'skills': skills,
                   'slots': slots + slots_receive,
                   'slots_available': slots_available})


@login_required(login_url="skill_sharing:login")
def add_skill(request):
    if request.method == 'POST':
        form = SkillAddForm(request.POST)
        if form.is_valid():
            user = request.user

            skill = Skill(skill_name=form.cleaned_data['skill_text'].capitalize(),)
            if Skill.objects.filter(skill_name__iexact=str(skill.skill_name)).exists():
                user.skill_set.add(Skill.objects.get(skill_name__iexact=str(skill.skill_name)))
                user.save()
            else:
                skill.save()
                user.skill_set.add(skill)
                user.save()

                activity = Activity(activity_name=form.cleaned_data['activity_text'],
                                    details=form.cleaned_data['details'],
                                    skill=skill)
                activity.save()

            return redirect('skill_sharing:home')
    else:
        form = SkillAddForm()
    return render(request, 'skill_sharing/add_skill.html', {'form': form})


@require_http_methods(["GET"])
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("skill_sharing:login"))
