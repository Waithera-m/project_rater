from django.shortcuts import render, redirect
from .models import Profile, Tags, Project
from django.views import generic
from .forms import RegistrationForm, ProjectsForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    """
    view function renders the landing page
    """
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects':projects})

@login_required(login_url='/accounts/login')
def user_profile(request, profile_id):
    """
    view function renders user's profile page
    """
    try:
        profile = Profile.objects.filter(id=profile_id)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'profile/profile.html', {'profile':profile})

@login_required(login_url='/accounts/login')
def add_project(request):
    """
    view function renders the template that displays project form
    """
    profiles = Profile.objects.all()
    current_user = request.user.profile
    for profile in profiles:
        if profile.user.id == request.user.id:
            if request.method == 'POST':
                form = ProjectsForm(request.POST, request.FILES)
                if form.is_valid():
                    project = form.save(commit=False)
                    project.creator = current_user
                    project.save()
                return redirect('projects:index')
            else:
                form = ProjectsForm()
    return render(request, 'projects/upload_project.html', {'form':form, 'profiles':profiles})
