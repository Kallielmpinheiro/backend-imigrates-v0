from django.db import models

# Create your models here.


class User(models.Model):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)