#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
import datetime
from django.utils import timezone
from shnam.lib.pbkdf2 import pbkdf2_check

# Create your models here.
class User(models.Model):
	userIdx = models.AutoField(primary_key=True, db_index=True)
	email = models.CharField(unique=True, max_length=50, blank=True, null=True)
	password = models.CharField(max_length=100)
	userId = models.CharField(unique=True, max_length=100, blank=True)
	device = models.CharField(max_length=50, blank=True, null=True)
	loginToken = models.TextField(default="", blank=True)
	createdTime = models.DateTimeField(auto_now_add=True)
	disabled = models.BooleanField(default=False)

	def __publish__(self):
		self.save()
		return self

	def check_password(self, password):
		return pbkdf2_check(password, self.password)

class Follow(models.Model):
	followIdx = models.AutoField(primary_key=True)
	follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
	followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followee")
	createdTime = models.DateTimeField(auto_now_add=True)
	disable = models.BooleanField(default=False)

	class Meta:
		unique_together = ('follower', 'followee')

	def __publish__(self):
		self.save()

class Playlist(models.Model):
	playlistIdx = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
	uri = models.CharField(max_length=100, null=True, blank=True)
	createdTime = models.DateTimeField(auto_now_add=True)
	disable = models.BooleanField(default=False)

	def __publish__(self):
		self.save()
	def __remove__(self):
		self.delete()

class MusicMsg(models.Model):
	msgIdx = models.AutoField(primary_key=True)
	followObj = models.ForeignKey(Follow, on_delete=models.CASCADE, related_name="follow_obj")
	# sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
	# receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
	uri = models.CharField(max_length=100, null=True, blank=True)
	createdTime = models.DateTimeField(auto_now_add=True)

	def __publish__(self):
		self.save()

class ErrorReport(models.Model):
    ErrorId = models.AutoField(primary_key=True)
    user = models.TextField(default="")
    callFunc = models.TextField(default="", blank=True)
    status = models.TextField(default="", blank=True)
    responseText = models.TextField(default="", blank=True)
    errmsg = models.TextField(default="", blank=True)
    createdTime = models.DateTimeField(auto_now=True)
    
    def __publish__(self):
        self.save()

