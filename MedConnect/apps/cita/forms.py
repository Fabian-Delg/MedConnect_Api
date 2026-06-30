from django import forms
from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'fecha_cita': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'hora_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo_consulta': forms.TextInput(attrs={'class': 'form-control'}),
            'presion_arterial': forms.TextInput(attrs={'class': 'form-control'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'temperatura': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_cita': forms.Select(attrs={'class': 'form-select'}),
        }