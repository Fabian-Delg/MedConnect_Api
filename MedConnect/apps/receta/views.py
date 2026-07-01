from django.shortcuts import render, redirect
from .models import Receta
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import RecetaSerializer

# Importa el conjunto de vistas genéricas para modelos de Django REST Framework
class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    permission_classes = [IsAuthenticated]