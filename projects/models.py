from django.db import models
from django.contrib.auth.models import User

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