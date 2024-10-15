# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# from ais.models.teachers import Teachers

# class Students(models.Model):
#     nim = models.CharField(max_length=10, unique=True)
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255, unique=True)
#     phone_number = models.CharField(max_length=13, unique=True)
#     year = models.IntegerField() # Tahun angkatan atau tahun masuk
#     teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE) # Relasi ke tabel Teachers

# def __str__(self):
#     return self.name

from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ais.models.teachers import Teachers

class Students(models.Model):
    nim = models.CharField(max_length=20, unique=True) # NIM biasanya berupa string
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    year = models.IntegerField() # Tahun angkatan atau tahun masuk
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE) # Relasi ke tabel Teachers
    
    def __str__(self):
        return self.name

   