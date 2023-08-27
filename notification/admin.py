from django.contrib import admin

from .models import *

# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["title", "message"]
    list_filter = ["title", "message"]
    search_fields = ["message", "title"]
    exclude = ["is_opened"]


admin.site.register(Notification, NotificationAdmin)


class UserMessageAdmin(admin.ModelAdmin):
    list_display = [ "user", "title", "body"]
    list_filter = ["user","title", "body"]
    search_fields = ["user","body", "title"]
    readonly_fields = ["user","created_at","body", "title"]


admin.site.register(UserMessages, UserMessageAdmin)
