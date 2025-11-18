cars = ['audi', 'bmw', 'chevrolet', 'corvette', 'tesla']

for car in cars:
    if car == "bmw" or car=="tesla":
        print(car.upper())
    else:
        print(car)

print("\n ---CONDICIONAL---")
# Condicionales: El condicional es el corazon del if.
# Condicional true
car = 'bmw'
print(car == 'bmw') # Salida -> True

# Condicional false
car2 = 'Audi'
print(car2 == 'audi') # Salida -> False

# Condicional true con lower()
car2 = 'Audi'
print(car2.lower() == 'audi') # Salida -> True

# Condicional != para determinar desigualdad
requested_topping = 'mushrooms' # -> String
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Comparaciones numericas
age = 18
print(age == 18) # True

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta. Intenta de nuevo!")

age = 19
print(age < 21)  # True
print(age <= 21) # True
print(age > 21)  # False
print(age >= 21) # False

#.Multiple conditions  
age_0 = 22
age_1 = 18

print("Multiples condiciones")
print("Operacion or - pseint (O)")
print( age_0 >= 21 or age_1 >= 21)
print( age_0 >= 21 or age_1 >= 18)

print("Multiples condiciones")
print("Operacion and - pseint (Y)")
print( age_0 >= 21 and age_1 >= 21)
print( age_0 >= 21 and age_1 >= 18)

print("\n A value is in a list")
# ¿Como nos preguntamos si algun valor esta en una lista?
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # True
print('pepperoni' in requested_toppings) # False

# A value not in a list
banned_users = ['gabriel', 'max', 'andrik', 'quevedo', 'chris', 'angel']
user = 'pedro'
print(user not in banned_users) # True

# Variables de tipo BOOLEANOS
game_active = True
can_edit = False

"""
if statement

if condition:
    do something

if condition:
    do something (True)
else:
    do something (False)
"""

# Preguntar la edad del usuario y decirle si tiene la edad suficiente para votar.
# input("") -> str

try:
    age = input("Escribe tu edad: ")
    if int(age)>=18:
      print("Tienes la edad suficiente para votar.")
    else:
      print("No tienes la edad suficiente para votar.")   

except:
    print("Error, ingresaste un caracter no valido")

print("Holi Charly")
