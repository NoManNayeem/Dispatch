# chat/admin.py

from django.contrib import admin
from .models import Chat, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 1  # How many empty message forms to show

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_participants', 'created_at')
    inlines = [MessageInline]

    def display_participants(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])
    display_participants.short_description = 'Participants'

class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sender', 'content', 'timestamp')
    list_filter = ('chat', 'sender', 'timestamp')
    search_fields = ('content',)

# Register models
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
