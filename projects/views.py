from django.shortcuts import render
from .models import Profile, Tags, Project
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    """
    class returns the landing page
    """
    model = Project
    template_name = 'projects/index.html'

    def get_queryset(self):
        """
        function returns added projects
        """
        return Profile.objects.all().order_by('-pub_date')
