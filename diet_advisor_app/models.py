from django.db import models

from user_app.models import CustomUser

class UserProfileModel(models.Model):

    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    
    age = models.IntegerField()

    gender = models.CharField(max_length=30,choices=[
          ('male','male'),
          ('female','female')
    ])

    height = models.FloatField()

    weight = models.FloatField()

    activity_level = models.CharField(max_length=100,choices=[
        ('sedentary','sedentary'),
        ('lightly active','lightly active'),
        ('moderately active','moderately active'),
        ('very active','very active')
    ])

    goal = models.CharField(max_length=100,choices=[
        ('lose weight','lose weight'),
        ('gain weight','gain weight'),
        ('maintain weight','maintain weight')
    ])
  