from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticated]