# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department,EmployeeType,Employee
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeType)
