from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)
    documento_identidad = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    tipo_sangre = models.CharField(max_length=5)
    alergias_conocidas = models.TextField()

    def __str__(self):
        return self.nombre_completo