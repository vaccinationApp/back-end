# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Farmer,Village,Region,Oblast,Country,RuralDistrict

admin.site.register(Country)
admin.site.register(Oblast)
admin.site.register(Region)
admin.site.register(RuralDistrict)
admin.site.register(Village)
admin.site.register(Farmer)






