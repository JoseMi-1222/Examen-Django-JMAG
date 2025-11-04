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


    





