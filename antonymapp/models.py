#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()

class WordPair1(models.Model):
	word1 = models.TextField()
	word2 = models.TextField()
	ones = models.IntegerField(default=0)
	two = models.IntegerField(default=0)
	three = models.IntegerField(default=0)
	four = models.IntegerField(default=0)
	five = models.IntegerField(default=0)
	word_number = models.IntegerField(default=0)

	def calc_mean(self):
		nominator = self.ones+self.two+self.three+self.four+self.five
		if nominator != 0 :
			mean = int(round((self.ones*1+self.two*2+self.three*3+self.four*4+self.five*5)/nominator))
			return mean
		return 0

	def __str__(self):
		return self.word1+" "+self.word2

class WordPair2(models.Model):
	word1 = models.TextField()
	word2 = models.TextField()
	ones = models.IntegerField(default=0)
	two = models.IntegerField(default=0)
	three = models.IntegerField(default=0)
	four = models.IntegerField(default=0)
	five = models.IntegerField(default=0)
	word_number = models.IntegerField(default=0)

	def calc_mean(self):
		nominator = self.ones+self.two+self.three+self.four+self.five
		if nominator != 0 :
			mean = int(round((self.ones*1+self.two*2+self.three*3+self.four*4+self.five*5)/nominator))
			return mean
		return 0

	def __str__(self):
		return self.word1+" "+self.word2

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	word_index = models.IntegerField(default=0)


post_save.connect(save_profile, sender=User)