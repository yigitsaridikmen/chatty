from django.contrib import admin

# Register your models here.
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['username','message_text','created_at']
    search_fields = ['message_text','created_at']

admin.site.register(Message,MessageAdmin)

