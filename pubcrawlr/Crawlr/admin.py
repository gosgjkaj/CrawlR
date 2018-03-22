from django.contrib import admin
from Crawlr.models import Category, Route
from Crawlr.models import UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Route)
admin.site.register(UserProfile)
