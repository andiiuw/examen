from django.db import models

from django.contrib import admin

class Sala(models.Model):
    numero  =   models.CharField(max_length=250)
    capacidad  =   models.CharField(max_length=200)
    responsable  =   models.CharField(max_length=250)


    def __str__(self):
        return self.numero


class Pelicula(models.Model):
    nombre  =   models.CharField(max_length=200)
    formato  =   models.CharField(max_length=200)
    duracion  =   models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    destinatario  =   models.CharField(max_length=200)
    direccion  =   models.CharField(max_length=200)
    descripcion  =   models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Ciudad(models.Model):
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    pelicula  = models.ManyToManyField(Pelicula, through='Asignacion')

    def __str__(self):
        return self.sala

class Asignacion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    ciudad= models.ForeignKey(Ciudad, on_delete=models.CASCADE)



class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1


class CiudadAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)


# Create your models here.
