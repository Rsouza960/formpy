from django.shortcuts import render, redirect
from formulario.forms import SolicitacaoForm


def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = SolicitacaoForm()
    return render(request, 'index.html', data)

def create(request):
    form = SolicitacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('form')


