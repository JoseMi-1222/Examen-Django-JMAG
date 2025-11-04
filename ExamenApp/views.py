from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

# -------------------------------
# VISTA: Errores
# -------------------------------

def mi_error_404(request, exception=None):
    return render(request, "errores/404.html",None,None,404) 

def mi_error_500(request):
    return render(request, "errores/500.html",None,None,500)

def mi_error_403(request, exception=None):
    return render(request, "errores/403.html",None,None,403)

def mi_error_400(request, exception=None):
    return render(request, "errores/400.html",None,None,400) 

#-------------------------------
# VISTA: Página Inicial (Index)
#-------------------------------
def index(request):
    return render(request, "app/index.html")

#-------------------------------
# VISTA: Videojuegos Fantasy en Estados Unidos
#-------------------------------

def fantasy_unidos(request, videojuego, pais):
    fantasy_unidos = Videojuego.objects.filter(
        titulo__icontains=videojuego,
        estudio_desarrollo__sede__pais__icontains=pais
    )

    contexto = {
        'fantasy_unidos': fantasy_unidos
    }
    return render(request, "app/videojuegos_fantasy_unidos.html", contexto)

#-------------------------------
# VISTA: Videojuegos de Play Station o Sony con alta puntuación
#-------------------------------

def playstation_sony(request):
    playstation_sony = Videojuego.objects.all()
    playstation_sony = playstation_sony.filter(
        Q(videojuegoplataformas__plataforma__fabricante__icontains='Sony') |
        Q(videojuegoplataformas__plataforma__nombre__icontains='Play Station'),
        analisis__puntuacion__gt=75
    ).distinct()[:3]

    contexto = {
        'playstation_sony': playstation_sony
    }
    return render(request, "app/videojuegos_playstation_sony.html", contexto)

#-------------------------------
# VISTA: Videojuegos sin plataformas ordenados por ventas estimadas
#-------------------------------

def ventas_estimadas(request):
    ventas_estimadas = Videojuego.objects.prefetch_related('videojuego_plataformas')
    ventas_estimadas = ventas_estimadas.filter(
        videojuego_plataformas__isnull=True
    ).order_by('-ventas_estimadas')

    contexto = {
        'ventas_estimadas': ventas_estimadas
    }
    return render(request, "app/videojuegos_ventas_estimadas.html", contexto)

#-------------------------------
# VISTA: Estudios con análisis en un año concreto ordenados por puntuación
#-------------------------------

def estudios_analisis(request, anyo):
    estudios_analisis = Estudio.objects.filter(
        videojuego__analisis__anyo_analisis=anyo
    ).order_by('-videojuego__analisis__puntuacion').distinct()

    contexto = {
        'estudios_analisis': estudios_analisis
    }
    return render(request, "app/estudios_analisis.html", contexto)





    





