from django.contrib import admin
from .models import Mensagem, SalaChat

class MensagemAdmin(admin.ModelAdmin):
    pass

class SalaChatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mensagem, MensagemAdmin)
admin.site.register(SalaChat, SalaChatAdmin)