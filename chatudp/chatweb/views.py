from django.shortcuts import render
from .models import SentTextMessage, ReceivedTextMessage

def home(request):
    # desabilitado temporariamente
    # fazer um merge do dos resultados de SentTextMessage, ReceivedTextMessage
    # exibir uma timeline dos resultados
    return render(request, 'chatweb/home.html')
