from django.urls import path
from . import views

urlpatterns = [
    # Página inicial (Index)
    path('', views.index, name='index'),
    path('fantasy_unidos/<str:videojuego>/<str:pais>/', views.fantasy_unidos, name='fantasy_unidos'),
    path('playstation_sony/', views.playstation_sony, name='playstation_sony'),
    path('ventas_estimadas/', views.ventas_estimadas, name='ventas_estimadas'),
    path('estudios_analisis/<int:anyo>/', views.estudios_analisis, name='estudios_analisis'),
    path('estudios_media_puntuacion/<str:estudio>/', views.estudios_media_puntuacion, name='estudios_media_puntuacion'),
    

]