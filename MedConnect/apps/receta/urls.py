from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_recetas, name='lista_recetas'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('agregar/', views.agregar_recetas, name='agregar_recetas'),
    path('editar/<int:id>/', views.editar_receta, name='editar_receta'),
    path('eliminar/<int:id>/', views.eliminar_receta, name='eliminar_receta'),
]