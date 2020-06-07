from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile
from django.conf import settings

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    method creates a new profile instance for a registered user
    """
    if created and not settings.TESTING:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    method saves created profile instance
    """
    if not settings.TESTING:
        instance.profile.save()
    