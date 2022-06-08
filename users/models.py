from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class User(AbstractUser):
    role = models.CharField(max_length=30, default="N/A")

    def __Str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Doctor(models.Model):
    user = models.OneToOneField(
        User, related_name="doctor", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)
    speciality = models.CharField(max_length=200)

    def __Str__(self):
        return self.full_name


class Hospital(models.Model):
    user = models.OneToOneField(
        User, related_name="hosptal", on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=250)

    def __Str__(self):
        return self.hospital_name
