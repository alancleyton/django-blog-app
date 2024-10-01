from django.contrib import admin
from django.http import HttpRequest
from website.models import MenuLinkModel, WebsiteSetupModel

@admin.register(MenuLinkModel)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'url')

@admin.register(WebsiteSetupModel)
class WebsiteSetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request: HttpRequest) -> bool:
        # not allows adding more than one website setup
        return not WebsiteSetupModel.objects.exists()
