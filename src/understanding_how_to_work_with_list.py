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
Python utiliza la identacion para determonar cuando una linea
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