from django.shortcuts import render, redirect
from .models import Profile, Tags, Project
from django.views import generic
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

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
