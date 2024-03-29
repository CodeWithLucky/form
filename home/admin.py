from django.contrib import admin
from . models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'description', 'start_date', 'is_completed'
    ]


admin.site.register(Task, TaskAdmin)