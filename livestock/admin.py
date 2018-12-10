# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Suit,TypesofLiveStock,LiveStock,Sex
admin.site.register(LiveStock)
admin.site.register(TypesofLiveStock)
admin.site.register(Suit)
admin.site.register(Sex)