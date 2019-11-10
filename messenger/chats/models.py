from django.db import models

class Chat(models.Model):
    is_group_chat = models.BooleanField()
    topic = models.CharField('Заглавие', max_length=50)
    last_message = models.CharField(max_length=50)  

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

class Message(models.Model):
    content = models.TextField()
    added_at = models.DateTimeField()
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.DO_NOTHING,
        verbose_name='Пользователь',
    )
    chat = models.ForeignKey(
        to='Chat',
        on_delete=models.DO_NOTHING,
        verbose_name='Чат',
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('-added_at',)

class Attachment(models.Model):
    form = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.DO_NOTHING,
        verbose_name='Пользователь',
    )
    chat = models.ForeignKey(
        to='Chat',
        on_delete=models.DO_NOTHING,
        verbose_name='Чат',
    )
    message = models.ForeignKey(
        to='Message',
        on_delete=models.DO_NOTHING,
        verbose_name='Сообщение',
    )

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Приложенный файл'
        verbose_name_plural = 'Приложенные файлы'
