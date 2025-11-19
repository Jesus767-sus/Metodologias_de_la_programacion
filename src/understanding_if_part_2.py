# <>
age = 0
try:
    age = int(input("Escribe tu edad: "))

except:
    age = -1
    print("Error, ingresaste un caracter no valido")
# <>
if age >= 100:
    print("Tienes mas de un siglo")
elif age >= 18 and age < 100:
    print("Eres mayor de edad")
elif age >= 0 and age < 18:
    print("Eres menor de edad")
else:
    print("Tuviste un error")

print("Holi Charly")   

"""
Hacer un programa que pregunte la edad de una persona y responda lo siguiente:
  - Si la edad es menor a 18, pero mayor que 4 entonces la entrada cuesta
  $200
  - Si la edad es mayor o igual a 18, entonces la entrada cuesta $400"""

if age <= 4 and age >= 0:
    print("Tu entrada es gratuita")
elif age > 4 and age < 18:
    print("Tu entrada cuesta $200")
elif age > 18:
    print("Tu entrada cuesta $400")

# Multiple if
guisos = ["deshebrada", "asado", "salsa verde", "pozole"]
if "asado" in guisos:
    print("Si hay asado")
else:
    print("No hay asado")
if "tamales" in guisos:
    print("Si hay tamales")
else:
    print("No hay tamales")

if "salsa verde" in guisos:
    print("Si hay salsa verde")
else:
    print("No hay tamales")

# Lista vacia
guisos = []
if guisos:
    print("Hay guisos")
else:
    print("No hay guisos")

# Utilizando varias listas
guisos_disponibles = ["Salsa verde", "deshebrada", "mole"]
guisos_a_ordenar = ["deshebrada", "caldo de iguana"]

print("¿Que guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    print(f"Deseo {guiso}")
    if guiso in guisos_disponibles:
        print(f"Si tenemos {guiso}")
    else:
        print("No tenemos de ese guiso")
print("Realizando pedido.....")
