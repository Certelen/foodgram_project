from django.contrib import admin

from .models import Tags


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
