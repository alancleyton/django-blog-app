from django.contrib import admin
from django.http import HttpRequest
from website.models import MenuLinkModel, WebsiteSetupModel

@admin.register(MenuLinkModel)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'url')

class MenuLinkInline(admin.TabularInline):
    model = MenuLinkModel
    extra = 1

@admin.register(WebsiteSetupModel)
class WebsiteSetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = (MenuLinkInline,)

    def has_add_permission(self, request: HttpRequest) -> bool:
        # not allows adding more than one website setup
        return not WebsiteSetupModel.objects.exists()
