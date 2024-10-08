from django.db import models
from utils.model_validators import validate_image

# Create your models here.

class MenuLinkModel(models.Model):
    class Meta:
        verbose_name = 'Menu link'
        verbose_name_plural = 'Menu links'

    text = models.CharField(max_length=50)
    url = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    website_setup = models.ForeignKey(
        'WebsiteSetupModel', on_delete=models.CASCADE,
        blank=True, null=True, default=None
    )

    def __str__(self) -> str:
        return self.text

class WebsiteSetupModel(models.Model):
    class Meta:
        verbose_name = 'Website setup'
        verbose_name_plural = 'Website setups'

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_header = models.BooleanField(default=False)
    show_search = models.BooleanField(default=False)
    show_menu = models.BooleanField(default=False)
    show_description = models.BooleanField(default=False)
    show_pagination = models.BooleanField(default=False)
    show_footer = models.BooleanField(default=False)
    favicon = models.ImageField(
        upload_to='assets/favicon/%y/%m',
        blank=True, default='',
        validators=[validate_image]
    )

    def __str__(self) -> str:
        return self.title

