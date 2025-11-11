"""
squares=[]
for value in range(0.11)
square = value**2
square.append(square)
print(squares)
"""
"""
 Una list comprehensions combina el ciclo for y la creacion
 de nuevos elementos en una sola linea y automaticamente
 agrega cada nuevo elemento a la lista es decir sin utilizar
 el metodo append.
"""
squares = [value**2 for value in range(0,11)]
# Para generar los numeros pares de entre 0 y el 100.
print("Numeros pares del 0 al 100 ")
squares_range = [value for value in range(0,101,2)]
evens_if = [value for value in range(0,101) if value%2==0]
print(evens_if)
print("Numeros impares del 1 al 100")
impar_if = [value for value in range(0,101) if value%2==1]
print(impar_if)
