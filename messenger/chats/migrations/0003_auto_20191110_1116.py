# Generated by Django 2.2.5 on 2019-11-10 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20191029_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'Приложенный файл', 'verbose_name_plural': 'Приложенные файлы'},
        ),
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Чат', 'verbose_name_plural': 'Чаты'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-added_at',), 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='attachment',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chats.Chat', verbose_name='Чат'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chats.Message', verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='topic',
            field=models.CharField(max_length=50, verbose_name='Заглавие'),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chats.Chat', verbose_name='Чат'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
