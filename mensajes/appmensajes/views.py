from django.shortcuts import render
from datetime import date
from .mensajes_data import MENSAJES

# Create your views here.

FECHA_INICIO = date(2026, 10, 10)

def vista_mensaje(request):
    dias_transcurridos = (date.today() - FECHA_INICIO).days
    indice = dias_transcurridos % len(MENSAJES)
    mensaje = MENSAJES[indice]

    return render(request, "appmensajes/mensaje.html", {"mensaje": mensaje})

# proyectos\venv-30-mensajes\mensajes\appmensajes\templates\mensaje.html