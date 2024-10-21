from django.contrib import admin
from .models import Profile, Friend

# Custom admin for Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'picture_preview')
    search_fields = ('user__username', 'bio')

    # This method provides a preview of the profile picture in the admin list view
    def picture_preview(self, obj):
        if obj.picture:
            return f'<img src="{obj.picture.url}" width="50" height="50"/>'
        return "No picture"
    
    picture_preview.allow_tags = True  # Allows HTML tags
    picture_preview.short_description = 'Profile Picture'

# Custom admin for Friend model
class FriendAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'is_accepted', 'created_at')
    search_fields = ('from_user__username', 'to_user__username')
    list_filter = ('is_accepted', 'created_at')

# Register the models and custom admin configurations
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Friend, FriendAdmin)
