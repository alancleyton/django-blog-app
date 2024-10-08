from django.core.exceptions import ValidationError
from django.db.models import ImageField

def validate_image(image: ImageField) -> None:
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Invalid image file format.')
