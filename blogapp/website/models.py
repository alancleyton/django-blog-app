from django.db import models

# Create your models here.

class ModelMenuLink(models.Model):
    text = models.CharField(max_length=50)
    url = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text
