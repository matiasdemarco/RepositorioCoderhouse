from django.http import HttpResponse
from .models import *
from django.template import loader
from django.shortcuts import render
from AppBnh.forms import CursoHeroes, CursoVillanos, CursoAntiHeroes

# Create your views here.
def inicio(request):
    return render (request, 'bnh/inicio.html')

def heroes(request):
    heroe1=Heroes(nombre="Izuku",apellido="Midoriya",poder="One For All",edad=18)
    heroe1.save()
    heroe2=Heroes(nombre="Kaksuki",apellido="Bakugo",poder="Nitroglicerina",edad=19)
    heroe2.save()
    return render (request, 'bnh/heroes.html')


def villanos(request):
    return render (request,'bnh/villanos.html')


def antiheroes(request):
    return render (request,'bnh/antiheroes.html')

def cursoheroes (request):
    if request.method=="POST":
        form=CursoHeroes(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nom=informacion["nombre"]
            ape=informacion["apellido"]
            pod=informacion["poder"]
            eda=informacion["edad"]

            curso1=Heroes(nombre=nom,apellido=ape,poder=pod,edad=eda)
            curso1.save()
            return render (request, 'bnh/inicio.html')
    else:
        formulario=CursoHeroes()    

    return render(request,'bnh/cursoheroes.html', {"form":formulario})



def cursovillanos (request):
    if request.method=="POST":
        form=CursoVillanos(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nom=informacion["nombre"]
            ape=informacion["apellido"]
            pod=informacion["poder"]
            eda=informacion["edad"]

            curso1=Villanos(nombre=nom,apellido=ape,poder=pod,edad=eda)
            curso1.save()
            return render (request, 'bnh/inicio.html')
    else:
        formulario=CursoVillanos()    

    return render(request,'bnh/cursovillanos.html', {"form":formulario})

def cursoantiheroes (request):
    if request.method=="POST":
        form=CursoAntiHeroes(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nom=informacion["nombre"]
            ape=informacion["apellido"]
            pod=informacion["poder"]
            eda=informacion["edad"]

            curso1=AntiHeroes(nombre=nom,apellido=ape,poder=pod,edad=eda)
            curso1.save()
            return render (request, 'bnh/inicio.html')
    else:
        formulario=CursoAntiHeroes()    

    return render(request,'bnh/cursoantiheroes.html', {"form":formulario})


def buscarheroe(request):
    return render (request, 'bnh/buscarheroe.html')


def buscar(request):
    if request.GET['Heroe']:
        Heroe=request.get[Heroe]
        heroes=Heroes.objects.all
        return render (request,'bnh/resultado.html',{"Heroes":heroes})
    else:
        return render (request,'bnh/buscarheroe.html', {"mensaje":"El heroe no existe"})
