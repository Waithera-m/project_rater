from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Tags, Project, Votes
from django.views import generic
from .forms import RegistrationForm, ProjectsForm, VotesForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, PostSerializer
from rest_framework import status
from .permissions import IsAuthenticatedOrReadOnly

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
    projects = Project.objects.filter(id=profile_id)
    return render(request, 'profile/profile.html', {'profile':profile, 'projects':projects})

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

@login_required(login_url='/accounts/login')
def search_by_project_title(request):
    """
    view function renders template that displays search results
    """
    if 'project' in request.GET and request.GET['project']:
       search_term = request.GET.get('project')
       projects = Project.search_by_title(search_term)
       message = f'{search_term}'
       return render(request, 'projects/results.html', {'message':message, 'projects':projects})
    else:
        message = 'Please enter a search term'
        return render(request, 'projects/results.html', {'message':message}) 

class DetailView(generic.DetailView):
    """
    class renders view that displays project-specific details
    """
    model = Project
    template_name = 'projects/detail.html'

    def get_queryset(self):
        return Project.objects.all()

@login_required(login_url='/accounts/login')
def rate_project(request, project):
    """
    view function renders rating and results views
    """
    project = Project.objects.filter(title=project).first()
    current_user = request.user
    votes = Votes.objects.filter(project=project)
    if request.method == 'POST':
        form = VotesForm(request.POST)
        votes = form.save(commit=False)
        votes.rater = request.user
        votes.project = project
        votes.save()
        project_ratings = Votes.objects.filter(project=project)
        design_mean_rating = []
        for d_rating in project_ratings:
            design_mean_rating.append(d_rating.design)
            design_average = sum(design_mean_rating)/len(design_mean_rating)
        usability_mean_rating = []
        for u_rating in project_ratings:
            usability_mean_rating.append(u_rating.usability)
            usability_average = sum(usability_mean_rating)/len(usability_mean_rating)
        content_mean_rating = []
        for c_rating in project_ratings:
            content_mean_rating.append(c_rating.content)
            content_average = sum(content_mean_rating)/len(content_mean_rating)
        
        votes.save()
        return HttpResponseRedirect(request.path_info)
    else:
        form = VotesForm()
        project_ratings = Votes.objects.filter(project=project)
    return render(request, 'projects/rate.html', {'form':form, 'project':project, 'project_ratings':project_ratings})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    """
    view function renders form for creating new profile
    """
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('projects:index')
    else:
        form = ProfileForm()
    return render(request, 'projects/new_profile.html', {"form":form})

class ProjectList(APIView):
    """
    class view inherits from APIView
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostDescription(APIView):
    """
    class view inherits from APIView
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Http404
    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = PostSerializer(project)
        return Response(serializers.data)
    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = PostSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)