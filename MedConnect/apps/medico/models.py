from django.db import models

class Medico(models.Model):
    HORARIO_CHOICES = [
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
        ('Rotativo', 'Rotativo'),
    ]

    nombre_completo = models.CharField(max_length=100)
    numero_licencia = models.CharField(max_length=50, unique=True)
    especialidad = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    correo_institucional = models.EmailField()
    universidad_egreso = models.CharField(max_length=150)
    anios_experiencia = models.PositiveIntegerField()
    horario_turno = models.CharField(max_length=20, choices=HORARIO_CHOICES)
    estado_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'