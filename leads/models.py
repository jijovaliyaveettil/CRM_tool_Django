from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=20, blank=True)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

def post_user_create(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_create, sender=User)


