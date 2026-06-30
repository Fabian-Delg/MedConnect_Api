from django.db import models

# Modelo Citas
class Cita(models.Model):
    estados_cita_opciones = [
        ('Programada', 'Programada'),
        ('Cancelada', 'Cancelada'),
        ('Asistida', 'Asistida'),
    ]

    paciente = models.ForeignKey('paciente.Paciente', on_delete=models.CASCADE, null=True, blank=True)
    medico = models.ForeignKey('medico.Medico', on_delete=models.CASCADE, null=True, blank=True)
    fecha_cita = models.DateField()
    hora_inicio = models.TimeField()
    motivo_consulta = models.TextField()
    presion_arterial = models.CharField(max_length=20)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)
    estado_cita = models.CharField(max_length=20, choices=estados_cita_opciones)

    def __str__(self):
        return f"Cita {self.id} - {self.paciente}"