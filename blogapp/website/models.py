from django.db import models

# Create your models here.

class ModelMenuLink(models.Model):
    text = models.CharField(max_length=50)
    url = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text

class ModelWebsiteSetup(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_header = models.BooleanField(default=False)
    show_search = models.BooleanField(default=False)
    show_menu = models.BooleanField(default=False)
    show_description = models.BooleanField(default=False)
    show_pagination = models.BooleanField(default=False)
    show_footer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
