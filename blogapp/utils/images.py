from pathlib import Path
from django.conf import settings
from django.db.models import ImageField
from PIL import Image

def resize_image(image: ImageField, new_width=800, optimize=True, quality=60) -> Image:
    image_path = Path(settings.MEDIA_ROOT / image.name).resolve()
    image_file = Image.open(image_path)
    original_width, original_height = image_file.size

    if original_width <= new_width:
        image_file.close()
        return image_file

    new_height = round(new_width * original_height / original_width)
    new_image_file = image_file.resize((new_width, new_height), Image.LANCZOS)
    new_image_file.save(image_path, optimize=optimize, quality=quality)
    return new_image_file
