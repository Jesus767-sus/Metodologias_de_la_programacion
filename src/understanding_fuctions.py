### FUNCIONES
# Las funciones son bloques de codigo para realizar
# una tarea en especifico.

# Cuando queremos realizar la tarea que se ha definido 
# en la funcion, tenemos que llamar el nombre de la 
# funcion que realizar la accion.

"""
   Sintaxis de una funcion

   def nombre_funcion():
       acciones

    
    Ejemplo: vamos a definir una funcion que de un saludo a Christopher.

"""

def gretting_christopher():
   """
      Funcion para saludar a una persona llamada Christopher
   """
for i in range(6):
 print("Hello Christopher")

gretting_christopher()

def create_full_name(first_name, middle_name, last_name):
   full_name = f"{first_name} {middle_name} {last_name}".title()
   return full_name

first_name = input("Dame tu primer nombre: ")
middle_name = input("Dame tu segundo nombre: ")
last_name = input("Dame tu apellido: ")

generated_fullname = create_full_name(
  first_name.strip().lower(),
  middle_name.strip().lower(),
  last_name.strip().lower())
print(generated_fullname)

# Hazme un codigo para sumar dos numeros
def sumar_dos_numeros(numero1, numero2):
   suma = numero1 + numero2
   return suma
num1 = float(input("Dame el primer numero: "))
num2 = float(input("Dame el segundo numero: "))

resultado = sumar_dos_numeros(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")

