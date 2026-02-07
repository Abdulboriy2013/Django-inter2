from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField()
    manzil = models.CharField()
    parol = models.CharField()
    telefon = models.CharField()