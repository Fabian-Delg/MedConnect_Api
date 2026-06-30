from django.db import models

# Create your models here.

class Receta(models.Model):
    cita = models.ForeignKey('cita.Cita', on_delete=models.CASCADE)
    medicamento_principal = models.CharField(max_length=100)
    dosis_recomendada = models.CharField(max_length=50)
    frecuencia_consumo = models.CharField(max_length=50)
    duracion_tratamiento = models.CharField(max_length=50)
    indicaciones_especiales = models.TextField(blank=True, null=True)
    via_administracion = models.CharField(max_length=50)
    fecha_emision = models.DateField()
    requiere_control = models.BooleanField(default=False)

    def __str__(self):
        return self.medicamento_principal