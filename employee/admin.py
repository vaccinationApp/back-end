# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department,EmployeeType,Employee
from django.contrib import admin
from django.contrib.admin.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    readonly_fields = ('content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(LogEntry,LogEntryAdmin)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeType)
