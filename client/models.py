from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClientModel(models.Model):
    user = models.OneToOneField(User, related_name="client", on_delete=models.CASCADE)
    first_name = models.CharField("Ismi", max_length=150)
    last_name = models.CharField("Familiya", max_length=150)
    phone = models.CharField("telefon raq.", max_length=50)
    CHOICES = (
        ('andijon','Andijon'),
        ('farg`ona','Farg`ona'),
        ('namangan','Namangan'),
        ('toshkent','Toshkent'),
        ('sirdaryo','Sirdaryo'),
        ('jizzax','Jizzax'),
        ('samarqand','Samarqand'),
        ('qashqadaryo','Qashqadaryo'),
        ('surxondaryo','Surxondaryo'),
        ('navoiy','Navoiy'),
        ('buxoro','Buxoro'),
        ('xorazm','Xorazm'),
        ('qoraqalpog`iston','Qoraqalpog`iston'),
    )
    place = models.CharField(choices=CHOICES, max_length=150)

    def __str__(self):
        return self.first_name