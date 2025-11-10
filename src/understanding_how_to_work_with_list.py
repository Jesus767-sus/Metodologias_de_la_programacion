# Trabajando con listas.

"""
Recorrer una lista sin importar la cantidad de elementos que tenga.
"""

magicians = ["ron", "hermione", "harry"]

print(magicians[0], magicians[1], magicians[2])

for magican in magicians:
    print(magican)
    print(magican.upper())
    print(f"{magican.title()} ese fue un gran hechizo.")
    print(f"{magican.lower()} No podemos esperar para ver el siguiente hechizo.")

print("\nGracias a todos, fue un gran espectaculo.")
"""
Identacion:
Python utiliza la identacion para determinar cuando una linea
de codigo esta conectada a la linea de codigo anterior.

Basicamente, se utilizan 4 espacios en blanco para obligarnos
a escribir codigo ordenado y estructurado
"""

# No olvidemos identar

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)   
print(f"I can't wait to see your next trick, {magician.title()}")    

# Identacion inncecesaria
message = "Hola Python"
print(message)

"""
Las listas tambien pueden almacenar numeros y de hecho,
son ideales para eso.
Python ofrece una gran cantidad de herramientas que ayudan
a trabajar eficientemente con listas de numeros.
"""

# Metodo built-in rage()
"""
El metodo range() nos ayuda a crear facilmente series de numeros:
Ejemplo:
"""
print("Numeros del 0 al 9")
for value in range(10): # 10 numeros entre 0-9
    print(value)
print("Numeros del 1 al 9")
for value in range(1, 10): # 10 numeros entre 1-9
    print(value)

print("Numeros impares del 1 al 9")
for value in range(1,10,2): # 10 numeros entre 1 y 9
    print(value)
odd_numbers = list(range(1,10,2))
print(odd_numbers)
print("Numeros pares del 1 al 10")
for value in range(0,11,2):
    print(value)
even_numbers = list(range(0,11,2))
print(even_numbers)

print("Tabla del 9")
for value in range(0,91,9):
    print(value)
Tab_9 = list(range(0,91,9))
print(Tab_9)

# Cuadrados de los primeros 10 numero
Squares = []
for number in range(1, 11):
    square = number**2
    Squares.append(square)
print(Squares)

## Mas metodos built-in
# Metodo min()
print("Metodos built-in")
digits = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

# Metodo max()
digits = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))

# Metodo sum()
digits = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 0]
print(sum(digits))