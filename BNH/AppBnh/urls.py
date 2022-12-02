from django.urls import path
from AppBnh.views import *

urlpatterns = [
    
    path('',inicio, name='inicio'),
    path('heroes/',heroes, name= 'heroes'),
    path('villanos/',villanos,name='villanos'),
    path('antiheroes/',antiheroes, name='antiheroes'),
    path('cursoheroes/',cursoheroes, name='cursoheroes' ),
    path('cursovillanos/',cursovillanos, name='cursovillanos' ),
    path('cursoantiheroes/',cursoantiheroes, name='cursoantiheroes' ),
    path('buscarheroe/',buscarheroe, name='buscarheroe' ),
    path('buscar/', buscar, name='buscar' ),
]