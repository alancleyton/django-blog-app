from django.contrib import admin
from website.models import ModelMenuLink

@admin.register(ModelMenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'url')
