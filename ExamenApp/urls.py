from django.urls import path
from . import views

urlpatterns = [
    # Página inicial (Index)
    path('', views.index, name='index'),
    path('fantasy_unidos/<str:videojuego>/<str:pais>/', views.fantasy_unidos, name='fantasy_unidos'),
    path('playstation_sony/', views.playstation_sony, name='playstation_sony'),

]