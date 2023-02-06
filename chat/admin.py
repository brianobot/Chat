from django.contrib import admin

from .models import Message, ChatRoom

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', )


admin.site.register(ChatRoom)