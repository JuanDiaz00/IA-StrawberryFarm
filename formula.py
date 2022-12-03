# Importamos la biblioteca necesaria para trabajar con números y operaciones matemáticas
import math

# Definimos la función para calcular el porcentaje de efectividad del cultivo
def calculate_cultivation_effectiveness(terrain, conditions):
  # Definimos una constante que representa el nivel mínimo de humedad del suelo necesario para que las fresas crezcan bien
  MIN_SOIL_MOISTURE = 70

  # Definimos una constante que representa el nivel máximo de plagas que pueden tolerarse en el cultivo
  MAX_PEST_LEVEL = 30

  # Definimos una constante que representa el factor de influencia de cada condición en el resultado del cultivo
  TERRAIN_FACTOR = 0.3
  CONDITIONS_FACTOR = 0.7

  # Calculamos el resultado del cultivo en función del terreno y las condiciones
  result = TERRAIN_FACTOR * terrain + CONDITIONS_FACTOR
