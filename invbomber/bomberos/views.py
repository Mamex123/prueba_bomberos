from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import Articulos
from .forms import Articulosform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout





def crear(request):
    formulario = Articulosform(request.POST or None, request.FILES or None)
    
    if formulario.is_valid():
        formulario.save()
        return redirect('mensaje')
    
    return render(request, 'inventario/crear.html', {'formulario': formulario})

def inicio(request):
    return render(request, 'paginas/index.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

@login_required
def inventbomber(request):
    return render(request, 'paginas/inventario.html')

def mensaje(request):
    return render(request, 'paginas/mensaje.html')


def editar(request,id):
    articulo = Articulos.objects.get(id=id)
    formulario = Articulosform(request.POST or None, request.FILES or None, instance=articulo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('listado')  
    return render(request, 'inventario/editar.html', {'formulario': formulario})

def login(request):
    return render(request, 'registration/login.html')

def exit(request):
    logout(request)
    return redirect('inicio')

def eliminar(request, id):
    articulos = Articulos.objects.get(id=id)
    articulos.delete()
    return redirect ('listado')

def listado(request):
    articulos = Articulos.objects.all()  # Recuperar todos los objetos del modelo Articulos
    return render(request, 'inventario/listado.html', {'articulos': articulos})