from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    pass 

    dob = models.DateField("Date of Birth", null=True, blank=True)

    def get_absolute_url(self): 
        return reverse('my-account')