from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'autor']
    list_display = ['id', 'title', 'autor']


admin.site.register(Content, ContentAdmin)
