from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre_t = models.CharField(max_length=50)
    descripcion_t = models.CharField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado_t = models.BooleanField(default=True)

class Persona(models.Model):
    nombre_p = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    rut = models.IntegerField(null=True)
    direccion_p = models.CharField(max_length=150)
    email_p = models.CharField(max_length=100)
    edad_p = models.IntegerField(null=True)
