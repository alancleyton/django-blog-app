from django.contrib import admin
from django.http import HttpRequest
from website.models import ModelMenuLink, ModelWebsiteSetup

@admin.register(ModelMenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'url')

@admin.register(ModelWebsiteSetup)
class WebsiteSetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request: HttpRequest) -> bool:
        # not allows adding more than one website setup
        return not ModelWebsiteSetup.objects.exists()
