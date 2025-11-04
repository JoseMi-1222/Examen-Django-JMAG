from django.db import models

# Create your models here.

class Estudio(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()
    pais_origen = models.CharField(max_length=100)  

class Sede(models.Model):
    estudio = models.ForeignKey('Estudio', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)

class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    estudio_desarrollo = models.ForeignKey('Estudio', on_delete=models.CASCADE)
    videojuego_plataformas = models.ManyToManyField('Plataforma', through='VideojuegoPlataformas')
    ventas_estimadas = models.IntegerField(null=True)

class VideojuegoPlataformas(models.Model):
    videojuego = models.ForeignKey('Videojuego', on_delete=models.CASCADE)
    plataforma = models.ForeignKey('Plataforma', on_delete=models.CASCADE)

class Analisis(models.Model):
    videojuego = models.ForeignKey('Videojuego', on_delete=models.CASCADE)
    puntuacion = models.IntegerField(null=True)
    anyo_analisis = models.IntegerField(null=True)  
    media_puntuacion = models.FloatField(null=True)
    critico = models.CharField(max_length=100, null=True)
    
