from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticated]