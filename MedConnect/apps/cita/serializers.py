from rest_framework import serializers
from .models import Cita

class CitaSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.CharField(
        source='paciente.nombre_completo',
        read_only=True
    )

    medico_nombre = serializers.CharField(
        source='medico.nombre_completo',
        read_only=True
    )

    class Meta:
        model = Cita
        fields = [
            'id',
            'paciente',
            'medico',
            'fecha_cita',
            'hora_inicio',
            'motivo_consulta',
            'presion_arterial',
            'peso_kg',
            'temperatura',
            'estado_cita',
            'paciente_nombre',
            'medico_nombre',
        ]