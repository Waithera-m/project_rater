from rest_framework import serializers
from .models import Project, Profile
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):
    """
    class facilitates the serialization of user objects
    """
    projects = ProjectSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'profile', 'projects']

class ProfileSerializer(serializers.ModelSerializer):
    """
    class facilitates the serialization of profile objects
    """
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'profile_pic']

