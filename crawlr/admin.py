# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from crawlr.models import Category, Route, UserProfile

#Customisations for Admin Interface

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class RouteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

#Page registrations

admin.site.register(Category, CategoryAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(UserProfile)
