from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CitaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAuthenticated]