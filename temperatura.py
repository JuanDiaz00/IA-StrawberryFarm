# Importamos la biblioteca necesaria para leer datos desde el teclado
import input

# Definimos la clase que representa la inteligencia artificial que ayuda a cultivar fresas
class AI:
  def __init__(self):
    # Inicializamos la temperatura en 0
    self.temperature = 0

  # Definimos el método que se encargará de ingresar la temperatura y determinar si es adecuada para el cultivo de fresas
  def input_temperature(self):
    # Pedimos al usuario que ingrese la temperatura
    self.temperature = input("Ingresa la temperatura: ")

    # La temperatura óptima para el cultivo de fresas es entre 14 y 21 grados Celsius
    min_temperature = 14
    max_temperature = 21

    # Si la temperatura está entre 14 y 21 grados Celsius, devolvemos True (es decir, es adecuada para el cultivo de fresas)
    if self.temperature >= min_temperature and self.temperature <= max_temperature:
      return True

    # Si la temperatura no está entre 14 y 21 grados Celsius, devolvemos False (es decir, no es adecuada para el cultivo de fresas)
    else:
      return False

# Creamos una instancia de la clase AI
ai = AI()

# Llamamos al método input_temperature para determinar si la temperatura ingresada es adecuada para el cultivo de fresas
if ai.input_temperature():
  print("La temperatura es adecuada para el cultivo de fresas.")
else:
  print("La temperatura no es adecuada para el cultivo de fresas.")
