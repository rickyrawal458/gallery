from django.contrib import admin
from .models import Tag, List

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag','created', 'updated']
    list_filter = ['created', 'updated']



