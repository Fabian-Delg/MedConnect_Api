from django import forms
from .models import Receta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'
        widgets = {
            'cita': forms.Select(attrs={'class': 'form-control'}),
            'medicamento_principal': forms.TextInput(attrs={'class': 'form-control'}),
            'dosis_recomendada': forms.TextInput(attrs={'class': 'form-control'}),
            'frecuencia_consumo': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion_tratamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'indicaciones_especiales': forms.TextInput(attrs={'class': 'form-control'}),
            'via_administracion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_emision': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'requiere_control': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
