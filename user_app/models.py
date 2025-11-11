from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):  # already have username,password,first_name,l_name for custamisation import abstractuser instead of User

    mobile_number = models.CharField(max_length=10,unique=True)
    