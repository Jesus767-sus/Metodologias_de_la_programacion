# Lists 
"""
Las listas son elementos mutables.

 Las listas nos permiten almacenar informacion, en algun lugar la 
 cantidad de informacion que tenga: ya sea que tengas pocos segmentos
 o millones de segmentos.

 Se recomienda nombrar una variable de tipo lista en plural.
 En python los corchetes [] definen una lista, sus elementos van 
 separados por comas.
 Ejemplo:

"""
bicycles=['trek', 'canondale', 'redline', 'specialized', 'gigant']
print(bicycles)
print(bicycles[0].title())

# Los indices comienzan en 0 y terminan en n-1 donde n es el numero de elementos
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
print(bicycles[4].title())

# Accediendo al ultimo elemento.
print(bicycles[-1].title()) # Ultimo elemento.
print(bicycles[-2].title()) # Penultimo elemento.
print(bicycles[-5].title()) # Primer elemento.

# Utilizando valores de la lista.
message3 = "Mi primer bicicleta fue una " + bicycles[4].upper() + "."
print(message3)

message_f = f"Mi primer bicicleta fue una {bicycles[4].title()}."
print(message_f)

## Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista.")
print(bicycles)

print("Metodos de las listas para agregar elementos: . append(element)")
bicycles.append("ducatti")
print(bicycles)

