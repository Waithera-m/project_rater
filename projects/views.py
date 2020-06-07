from django.shortcuts import render, redirect
from .models import Profile, Tags, Project
from django.views import generic
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext

# Create your views here.
class IndexView(generic.TemplateView):
    """
    class returns the landing page
    """
    template_name = 'projects/index.html'
    def get_queryset(self):
        """
        function returns added projects
        """
        return Profile.objects.all().order_by('-pub_date')

