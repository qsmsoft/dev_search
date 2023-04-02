from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile


# @receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("Profile signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.user_name,
            email=user.email,
            name=user.first_name,
        )


# @receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("Deleting user...")


post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)
