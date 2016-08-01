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

class Friend(models.Model):
	friendIdx = models.AutoField(primary_key=True)
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
	createdTime = models.DateTimeField(auto_now_add=True)
	disable = models.BooleanField(default=False)

	class Meta:
		unique_together = ('sender', 'receiver')

	def __publish__(self):
		self.save()