# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Disease,Bloodtest,Medicine,Vaccination,Modeofapplication,TestMethod
admin.site.register(Vaccination)
admin.site.register(Disease)
admin.site.register(Medicine)
admin.site.register(Bloodtest)
admin.site.register(Modeofapplication)
admin.site.register(TestMethod)