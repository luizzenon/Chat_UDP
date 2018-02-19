from django.shortcuts import render
from .models import Mensagem

def home(request):
    mensagens = Mensagem.objects.all()
    return render(request, 'chatweb/home.html', {'mensagens':mensagens})
