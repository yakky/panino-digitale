from django.shortcuts import render


def lista_panini(request):
    return render(request, 'prenotazioni/lista_panini.html', {})
