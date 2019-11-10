from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Member(models.Model):
    new_messages = models.CharField(max_length=30)
    user = models.ForeignKey(
        to='User',
        on_delete=models.DO_NOTHING,
        verbose_name='Пользователь',
    )
    chat = models.ForeignKey(  
        to='chats.Chat',
        on_delete=models.DO_NOTHING,
        verbose_name='Чат',
    )
    last_read_message = models.ForeignKey(  
        to='chats.Message',
        on_delete=models.DO_NOTHING,
        verbose_name='Последнее прочитанное',
    )

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
