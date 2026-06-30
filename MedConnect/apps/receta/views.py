from django.shortcuts import render, redirect
from .models import Receta
from .forms import RecetaForm, RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# Página de inicio
def inicio(request):
    return redirect('login')

# Registro de usuarios 
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: 
        form = RegistroUsuarioForm()
    return render(request, 'base/registro.html', {'form':form})

# Login de usuarios 
def iniciar_sesion(request):
    if request.method == 'POST': 
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user:
            login(request, user)
            return redirect('lista_recetas')
        
    return render(request, 'base/login.html')

# Logout de usuarios
def cerrar_sesion(request):
    logout(request)
    return redirect('login')


# CRUD de recetas

@login_required 
def lista_recetas(request):
    recetas = Receta.objects.all()
    # renderiza la plantilla con la lista de recetas
    return render(request, 'recetas/lista.html',{'recetas': recetas})

@login_required
def agregar_recetas(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receta registrada correctamente.')
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recetas/form.html', {'form': form, 'titulo': 'Registrar Receta'})

@login_required
def editar_receta(request, id):
    receta = Receta.objects.get(id=id)
    form = RecetaForm(request.POST or None, instance=receta)
    if form.is_valid():
        form.save()
        return redirect('lista_recetas')
    
    return render(request, 'recetas/form.html', {'form':form})

@login_required
def eliminar_receta(request, id):
    receta = Receta.objects.get(id=id)
    receta.delete()
    return redirect('lista_recetas')