from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
from tasks.models import CustomUser, Task



class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_super_admin')
    list_filter = ('is_super_admin',)

admin.site.register(CustomUser, CustomUserAdmin)

LogEntry.__user_model = CustomUser


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
    list_editable = ('completed',)

admin.site.register(Task, TaskAdmin)