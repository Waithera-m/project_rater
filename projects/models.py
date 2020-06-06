from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    """
    class facilitates the creation of profile objects
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=70)
    location = models.CharField(max_length=60)
    profile_pic = models.ImageField(upload_to='profiles/')
    created_at = models.DateTimeField(auto_now_add=True)
    def save_profile(self):
        """
        method saves added profile
        """
        self.save()
    
    def update_profile(self, using=None, fields=None, **kwargs):
        """
        class method updates profile properties
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_profile(self):
        """
        method deletes saved profile
        """
        self.delete()

class Tags(models.Model):
    """
    class facilitates the creation of language objects
    """
    name = models.CharField(max_length=60)

    def save_tags(self):
        """
        method saves added tag
        """
        self.save()
    
    def update_tags(self, using=None, fields=None, **kwargs):
        """
        method updates saves tag
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_tags(self):
        """
        method deletes saved tag
        """
        self.delete()

class Project(models.Model):
    """
    class facilitates the creation of project objects
    """
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='projects/')
    description = HTMLField()
    live_link = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tags)
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)

