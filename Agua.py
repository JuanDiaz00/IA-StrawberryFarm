# Importamos la biblioteca necesaria para leer datos desde el teclado
import input

# Definimos la clase que representa la inteligencia artificial que ayuda a cultivar fresas
class AI:
  def __init__(self):
    # Inicializamos el nivel de agua en 0
    self.water_level = 0

  # Definimos el método que se encargará de saber si falta agua para regar las fresas
  def is_water_needed(self):
    # Pedimos al usuario que ingrese el nivel de agua
    self.water_level = input("Ingresa el nivel de agua: ")

    # Si el nivel de agua es menor a 50, devolvemos True (es decir, falta agua para regar las fresas)
    if self.water_level < 50:
      return True

    # Si el nivel de agua es mayor o igual a 50, devolvemos False (es decir, no falta agua para regar las fresas)
    else:
      return False

# Creamos una instancia de la clase AI
ai = AI()

# Llamamos al método is_water_needed para saber si falta agua para regar las fresas
if ai.is_water_needed():
  print("Falta agua para regar las fresas.")
else:
  print("No falta agua para regar las fresas.")
