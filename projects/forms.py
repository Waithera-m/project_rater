from django import forms
from .models import Profile, Project, Votes

class RegistrationForm(forms.Form):
    """
    class facilitates the creation of registration form objects
    """
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()
    bio = forms.CharField(max_length=70)

    def save(self):
        """
        method saves created user
        """
        new_user = Profile.objects.create(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            bio=self.cleaned_data['bio'],
        )
        return new_user

class ProjectsForm(forms.ModelForm):
    """
    class facilitates the generation of a form to facilitate the addition of new projects
    """
    class Meta:
        model = Project
        exclude = ['creator', 'design', 'usability', 'content', 'pub_date'] 

class VotesForm(forms.ModelForm):
    """
    class facilitates the generation of vote form objects
    """
    class Meta:
        model = Votes
        fields = ['design', 'usability', 'content']

class ProfileForm(forms.ModelForm):
    """
    class facilitates the creation of profile form objects
    """
    class Meta:
        model = Profile
        exclude = ['user']
         