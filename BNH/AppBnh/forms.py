from django import forms


class CursoHeroes(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    poder= forms.CharField(max_length=20)
    edad= forms.IntegerField()

class CursoVillanos(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    poder= forms.CharField(max_length=20)
    edad= forms.IntegerField()
    

class CursoAntiHeroes(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    poder= forms.CharField(max_length=20)
    edad= forms.IntegerField()
    