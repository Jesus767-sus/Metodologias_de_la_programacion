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