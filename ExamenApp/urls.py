from django.urls import path
from . import views

urlpatterns = [
    # Página inicial (Index)
    path('', views.index, name='index'),
]