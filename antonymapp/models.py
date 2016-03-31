from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()

class WordPair(models.Model):
	word1 = models.TextField()
	word2 = models.TextField()
	ones = models.IntegerField(default=0);
	two = models.IntegerField(default=0);
	three = models.IntegerField(default=0);
	four = models.IntegerField(default=0);
	five = models.IntegerField(default=0);

	def calc_mean():
		mean = int(round((ones*1+two*2+three*3+four*4+five*5)/(ones+two+three+four+five))
		return mean

	def __str__(self):
		return self.word1+" "+self.word2

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	score = models.IntegerField(default=0);

post_save.connect(save_profile, sender=User)