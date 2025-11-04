from django.db import models

# Create your models here.

"""
Dada la siguiente SQL, crea los Modelos, Urls y QuerySets correspondientes para mostrar los datos que se piden:

SELECT 
    V.*,E.*,VP.*,P.*
FROM 
    videojuego V
INNER JOIN 
    estudio E ON V.estudio_desarrollo_id = E.id
INNER JOIN 
    sede S ON E.id = S.estudio_id
LEFT JOIN 
    videojuego_plataformas VP ON V.id = VP.videojuego_id
LEFT JOIN
    plataforma P ON VP.plataforma_id = P.id
LEFT JOIN
    analisis A ON V.id = A.videojuego_id
WHERE 
    V.titulo LIKE '%Fantasy%' 
    AND S.pais LIKE '%Unidos%';
"""

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
    VideojuegoPlataformas = models.ManyToManyField('Plataforma', through='VideojuegoPlataformas')

class VideojuegoPlataformas(models.Model):
    videojuego = models.ForeignKey('Videojuego', on_delete=models.CASCADE)
    plataforma = models.ForeignKey('Plataforma', on_delete=models.CASCADE)

class Analisis(models.Model):
    videojuego = models.ForeignKey('Videojuego', on_delete=models.CASCADE)
