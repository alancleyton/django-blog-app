from django.http import HttpRequest
from website.models import WebsiteSetupModel

def website_setup(request: HttpRequest):
    setup = WebsiteSetupModel.objects.order_by('-id').first()
    return { 'website_setup': setup }
