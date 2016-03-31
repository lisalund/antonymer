from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from .signals import save_profile
# Create your models here.

def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	score = models.IntegerField(default=0);

post_save.connect(save_profile, sender=User)