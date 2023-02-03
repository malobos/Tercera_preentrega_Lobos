from django.db import models

class recCarne (models.Model):
    nombre= models.CharField(max_length=40)
    fechaDeSubida= models.DateField()
    ingredientes= models.CharField(max_length=200)

class recPastas (models.Model):
    nombre= models.CharField(max_length=40)
    fechaDeSubida= models.DateField()
    ingredientes= models.CharField(max_length=200)

class recVerduras(models.Model):
    nombre= models.CharField(max_length=40)
    fechaDeSubida= models.DateField()
    ingredientes= models.CharField(max_length=200)

class contacto(models. Model):
    nombre= models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    correo = models.EmailField() 