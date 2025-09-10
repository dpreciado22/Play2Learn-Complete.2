from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.core.files.images import get_image_dimensions

def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 2500 or h > 2500:
        raise ValidationError('Avatar must be no bigger than 800x800 pixels.')

class CustomUser(AbstractUser):
    dob = models.DateField("Date of Birth", null=True, blank=True)
    
    avatar = models.ImageField(
        upload_to='avatars/',
        null='true',
        blank=True,
        help_text='Image must be 200px by 200px.',
        validators=[validate_avatar],
    )

    def get_absolute_url(self): 
        return reverse("my-account")

    def __str__(self):
        return self.username