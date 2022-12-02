# Importamos el módulo necesario para trabajar con sensores
import sensors

# Definimos la clase que representa la inteligencia artificial que ayuda a cultivar fresas
class AI:
  def __init__(self):
    # Inicializamos el sensor de peso en 0
    self.weight_sensor = 0

    # Inicializamos el sensor de madurez en 0
    self.ripeness_sensor = 0

  # Definimos el método que se encargará de determinar cuándo es el momento óptimo para recolectar las fresas
  def optimal_harvest_time(self):
    # Leemos el valor del sensor de peso
    weight = self.weight_sensor.read()

    # Leemos el valor del sensor de madurez
    ripeness = self.ripeness_sensor.read()

    # Las fresas están en su punto óptimo de madurez cuando pesan entre 5 y 10 gramos
    min_weight = 5
    max_weight = 10

    # Las fresas están en su punto óptimo de madurez cuando tienen un nivel de madurez entre 75 y 100
    min_ripeness = 75
    max_ripeness = 100

    # Si el peso y el nivel de madurez están dentro del rango óptimo, devolvemos True (es decir, es el momento óptimo para recolectar las fresas)
    if weight >= min_weight and weight <= max_weight and ripeness >= min_ripeness and ripeness <= max_ripeness:
      return True

    # Si el peso o el nivel de madurez no están dentro del rango óptimo, devolvemos False (es decir, no es el momento óptimo para recolectar las fresas)
    else:
      return False

# Creamos una instancia de la clase AI
ai = AI()

# Llamamos al método optimal_harvest_time para determinar si es el momento
