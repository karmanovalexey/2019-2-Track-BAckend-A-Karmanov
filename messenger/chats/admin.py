from django.contrib import admin
from chats.models import Chat

class ChatAdmin(admin.ModelAdmin):
  list_filter=('id',)
  list_display=('id', 'topic',)

admin.site.register(Chat, ChatAdmin)
