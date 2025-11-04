from django.db import models

# Create your models here.

"""
Ejer 1
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
"""
Ejer 2
Dada la siguiente SQL, crea los Modelos, Urls y QuerySets correspondientes para mostrar los datos que se piden:

SELECT 
    V.*,E.*,VP.*,P.*
FROM 
    videojuego V
INNER JOIN 
    videojuego_plataformas VP ON V.id = VP.videojuego_id
INNER JOIN 
    plataforma P ON VP.plataforma_id = P.id
INNER JOIN
    analisis A ON V.id = A.videojuego_id
INNER JOIN 
    estudio E ON V.estudio_desarrollo_id = E.id
LEFT JOIN
    sede S ON E.id = S.estudio_id
WHERE 
    P.fabricante LIKE 'Sony' 
    OR p.nombre LIKE ‘%Play Station%’ 
    AND A.puntuacion > 75
LIMIT 3
"""
"""
Ejer 3
SELECT 
    V.*
FROM 
    videojuego V
LEFT JOIN 
    videojuego_plataformas VP ON V.id = VP.videojuego_id
WHERE 
    VP.id IS NULL
ORDER BY v.ventas_estimadas DESC

"""
"""_
Ejer 4
Crea los Modelos, Urls y QuerySets correspondientes, para que puedas obtener todos los Estudios que tengan videojuegos con una análisis en un año en concreto ordenados por puntuación del análisis de mayor a menor. En esta querySet si os salen duplicados, debéis usar distinct() después de construir la querySet completa para evitarlos.
"""
"""
Ejer 5
Crea los Modelos, Urls y QuerySets correspondientes, para que puedas obtener todos los videojuegos de un estudio de desarrollo en concreto que tengan una media de puntuación de análisis mayor que 7.5.
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
    
