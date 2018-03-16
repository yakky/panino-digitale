from django.shortcuts import render

from .models import Panino


def lista_panini(request):
    panini = Panino.objects.all()
    return render(request, 'prenotazioni/lista_panini.html', {'panini': panini})
