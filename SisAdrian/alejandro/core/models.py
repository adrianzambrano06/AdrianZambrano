from django.db import models

# Create your models here.
class nuevoUsuario(models.Model):
    nombreUsuario=models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    pwd = models.CharField(max_length=150)
    Edad=models.IntegerField()
    Genero = models.CharField(max_length=1)
    Estado = models.CharField(max_length=150)