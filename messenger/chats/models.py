from django.db import models
from users.models import User

class Chat(models.Model):
  is_group_chat = models.BooleanField()
  topic = models.CharField(max_length=50, null=False)
  last_message = models.CharField(max_length=50, null=False)

class Message(models.Model):
  user = models.ForeignKey(User, models.DO_NOTHING)
  chat = models.ForeignKey(Chat, models.DO_NOTHING)
  content = models.TextField()
  added_at = models.DateTimeField()

class Attachment(models.Model):
  user = models.ForeignKey(User, models.DO_NOTHING)
  chat = models.ForeignKey(Chat, models.DO_NOTHING)
  message = models.ForeignKey(Message, models.DO_NOTHING)
  form = models.CharField(max_length=50, null=False)
  url = models.CharField(max_length=50, null=False) 

class Member(models.Model):
  user = models.ForeignKey(User, models.DO_NOTHING)
  chat = models.ForeignKey(Chat, models.DO_NOTHING)
  new_messages = models.CharField(max_length=30, null=False)
  last_read_message_id = models.OneToOneField(Message, models.DO_NOTHING)
  