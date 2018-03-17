from django.shortcuts import redirect, render

from .forms import PaninoForm
from .models import Panino


def lista_panini(request):
    panini = Panino.objects.all()
    return render(request, 'prenotazioni/lista_panini.html', {'panini': panini})


def aggiungi_panino(request):
    if request.method == 'POST':
        form = PaninoForm(request.POST)
        if form.is_valid():
            panino = form.save()
            return redirect('lista-panini')
    else:
        form = PaninoForm()
    return render(request, 'prenotazioni/modifica_panino.html', {'form': form})
