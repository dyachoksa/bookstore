from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created: bool, **kwargs):
    if not created:
        return

    UserProfile.objects.create(user=instance)
