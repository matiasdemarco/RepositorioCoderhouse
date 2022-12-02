from django.db import models

# Create your models here.
class Heroes(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    poder= models.CharField(max_length=20)
    edad= models.IntegerField()

class Villanos(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    poder= models.CharField(max_length=20)
    edad= models.IntegerField()

class AntiHeroes(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    poder= models.CharField(max_length=20)
    edad= models.IntegerField()