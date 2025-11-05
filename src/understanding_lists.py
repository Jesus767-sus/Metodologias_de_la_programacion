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

"""
Agregar elementos a una lista.
- append(): Agrega un elemento al final de la lista.

"""
print("\n--- Agregar elementos a una lista metodo append()---")
motorcycles = ['honda', 'yamaha', 'susuky']
print(motorcycles) #Salida: ['honda', 'yamaha', 'susuky']
motorcycles.append('ducati')
print(motorcycles) #Salida: ['honda', 'yamaha', 'susuky', 'ducati']
"""
Agregar elementos en una posicion especifica
-insert(): Inserta un elemento en una posicion especifica.
""" 
print("\n--- Agregar elementos a una lista metodo insert()---")
motorcycles = ['honda', 'yamaha', 'susuky']
print(motorcycles) #Salida: ['honda', 'yamaha', 'susuky']
motorcycles.insert(1,'ducati')
print(motorcycles) #Salida: ['honda', 'ducati', 'susuky', 'yamaha']

"""
Eliminar elementos de una lista y usar el valor eliminado
- pop(): Elimina y devuelve el ultimo elemento de la lista.
"""
print("\n--- Eliminar elementos de una lista .pop()---")
motorcycles = ['honda', 'yamaha', 'susuky']
print(motorcycles) #Salida: ['honda', 'yamaha', 'susuky']
last_motocycles = motorcycles.pop()
print(motorcycles) #Salida: ['honda','yamaha']

"""
Eliminar un elemento especifico de una lista por valor
- pop(index): Elimina y devuelve el elemento en la posicion
especificada.
"""
print("\n--- Eliminar un elemento especifico .pop(index)---")
motorcycles = ['honda', 'yamaha', 'susuky']
print(motorcycles) #Salida: ['honda', 'yamaha', 'susuky']
last_motocycles = motorcycles.pop(1)
print(motorcycles) #Salida: ['honda','susuky']

"""
Elimina un elemento especifico de una lista por valor
- remove(): Elimina la primera aparicion de un valor especifico en
la lista
"""
print("\n--- Eliminar un elemento especifico de una lista por valor metodo remove---")
motorcycles = ['honda', 'yamaha', 'susuky', 'ducati']
print(motorcycles) #Salida: ['honda', 'yamaha', 'susuky', 'ducati']
motorcycles.remove('ducati')
print(motorcycles) #Salida: ['honda','yamaha','susuky']
print("\n")

"""
Organizar una lista permanentemente
-sport(): Ordena la lista en orden alfabetico.
"""
print("\n--- Organizar una lista permanentemente metodo sport---")
motorcycles = ['honda', 'yamaha', 'susuky', 'ducati']
print(motorcycles) #Salida: ['honda', 'yamaha', 'susuky', 'ducati']
motorcycles.sort()
print(motorcycles) #Salida: ['ducati', 'honda', 'susuky', 'yamaha']
print("\n")
motorcycles.sort(reverse=True)
print(motorcycles)
