from django.shortcuts import render
from datetime import date
from .mensajes_data import MENSAJES
from .models import FotoGaleria
from pathlib import Path

# Create your views here.

def hub(request):
    return render(request, 'appmensajes/hub.html')

FECHA_INICIO = date(2026, 10, 10)

EXTENSIONES = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
CARPETA_FOTOS = Path(__file__).resolve().parent / 'static' / 'galeria'

def vista_mensaje(request):
    dias_transcurridos = (date.today() - FECHA_INICIO).days
    indice = dias_transcurridos % len(MENSAJES)
    mensaje = MENSAJES[indice]

    return render(request, "appmensajes/mensaje.html", {"mensaje": mensaje})

def vista_notificacion(request):
    return render(request, 'appmensajes/notificacion.html')


def vista_galeria(request):
    fotos = []
    if CARPETA_FOTOS.exists():
        for archivo in sorted(CARPETA_FOTOS.iterdir()):
            if archivo.suffix.lower() in EXTENSIONES:
                fotos.append({
                    'archivo': archivo.name,
                    'descripcion': '',
                })
    return render(request, 'appmensajes/galeria.html', {'fotos': fotos})
