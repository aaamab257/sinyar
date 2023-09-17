from django.contrib import admin

from .models import *

# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["title", "message"]
    list_filter = ["title", "message"]
    search_fields = ["message", "title"]
    exclude = ["is_opened"]

    def has_view_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Customize the queryset, e.g., filter by user or order by timestamp
        return qs

    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['unread_count'] = self.get_queryset(request).filter(is_opened=False).count()
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Notification, NotificationAdmin)


class AdminNotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'timestamp', 'is_read')

    def has_view_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Customize the queryset, e.g., filter by user or order by timestamp
        return qs

    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['unread_count'] = self.get_queryset(request).filter(is_read=False).count()
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(AdminNotification, AdminNotificationAdmin)




class UserMessageAdmin(admin.ModelAdmin):
    list_display = [ "user", "title", "body"]
    list_filter = ["user","title", "body"]
    search_fields = ["user","body", "title"]
    readonly_fields = ["user","created_at","body", "title"]

    def has_view_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True


admin.site.register(UserMessages, UserMessageAdmin)
