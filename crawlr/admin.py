# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from crawlr.models import Category, Page, UserProfile

#Customisations for Admin Interface

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

#Page registrations

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)