from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class User(models.Model):
	userIdx = models.AutoField(primary_key=True, db_index=True)
	userId = models.CharField(unique=True, max_length=50)
	email = models.CharField(max_length=50, blank=True, null=True)
	password = models.CharField(max_length=100)
	device = models.CharField(max_length=50, blank=True, null=True)
	loginToken = models.TextField(default="", blank=True)
	createdTime = models.DateTimeField(auto_now_add=True)
	disabled = models.BooleanField(default=False)

	def __publish__(self):
		self.save()
		return self

