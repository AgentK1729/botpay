from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Transaction(models.Model):
	sender = models.CharField(max_length=50)
	receiver = models.CharField(max_length=50)
	amount = models.FloatField(max_length=5)
	
class ChatMessage(models.Model):
	# 0 flag means user to bot, 1 means bot to user
	user = models.ForeignKey(User)
	message = models.CharField(max_length=100)
	reply = models.CharField(max_length=100)
	flag = models.IntegerField(max_length=1)
	
admin.site.register(Transaction)
admin.site.register(ChatMessage)