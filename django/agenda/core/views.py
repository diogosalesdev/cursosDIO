from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

#def index(request) :s
#  return redirect('/agenda')

def lista_eventos(request):
  usuario = request.user
  evento = Evento.objects.all()
  data = {'eventos' :evento}
  return render(request, 'agenda.html', data)
