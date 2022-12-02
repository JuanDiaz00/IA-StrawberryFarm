# Importamos la biblioteca necesaria para trabajar con datos de tiempo
import datetime

# Definimos la clase AI para cultivar fresas
class AI:
  # Inicializamos la inteligencia artificial
  def __init__(self):
    # Asignamos valores iniciales a los atributos que se utilizarán en el programa
    self.last_watered = datetime.datetime.now()
    self.soil_moisture = 50
    self.fertilizer_level = 75
    self.pest_level = 0

  # Definimos el método para regar las fresas
  def water_strawberries(self):
    # Aumentamos el nivel de humedad del suelo y actualizamos la fecha de la última vez que se regó
    self.soil_moisture += 10
    self.last_watered = datetime.datetime.now()

  # Definimos el método para aplicar fertilizante a las fresas
  def fertilize_strawberries(self):
    # Aumentamos el nivel de fertilizante y disminuimos el nivel de humedad del suelo
    self.fertilizer_level += 10
    self.soil_moisture -= 10

  # Definimos el método para controlar las plagas en las fresas
  def control_pests(self):
    # Disminuimos el nivel de plagas
    self.pest_level -= 10

  # Definimos el método para recoger las fresas maduras
  def harvest_strawberries(self):
    # Mostramos un mensaje indicando que las fresas se han cosechado
    print("¡Las fresas se han cosechado!")

# Creamos una instancia de la clase AI
ai = AI()

# Llamamos a los métodos necesarios para cultivar fresas
ai.water_strawberries()
ai.fertilize_strawberries()
ai.control_pests()
ai.harvest_strawberries()
