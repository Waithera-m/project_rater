from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    class facilitates the serialization of project objects
    """
    class Meta:
        model = Project
        fields = ('title', 'creator', 'project_image', 'description', 'tags', 'live_link')

class PostSerializer(serializers.ModelSerializer):
    """
    class facilitates the serialization of a single project object
    """
    class Meta:
        model = Project
        fields = ('id', 'title', 'creator', 'project_image', 'description', 'tags', 'live-link')