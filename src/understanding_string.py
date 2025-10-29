"""
String variables

Un string es de manera sencilla una serie de caracteres. En python, todo lo que se encuentre dentro de comillas simples o dobles sera considerado un string.

Ejemplos_
"Esto es un string"
'Esto tambien es un string'

'Le dije a un amigo "Python es mi lenguaje favorito" '
"El lenguaje 'Python' lleva el nombre oir Monty Python, no por la serpiente"
"""

name = "clase de programacion"
print(name)

# title
print(name.title())

"""

Un metodo es una accion que python puede realizar 
en un fragmento de datos o sobre una variable.

El punto . despues de una variable 
seguido del metodo titlee() dice que se tiene que ejecutar el metodo 
title de la variable name.

Todos los metodos van seguidos de parentesis porque en ocaciones
necesitan informacion adicional para funcionar la cual 
la informacion iria dentro de los parentesis.
En esta ocacion, el metodo .title() no requiere informacion adicional 
para funcionar. 

"""
print("Metodo upper: ", name.upper())
print("Metodo lower: ", name.lower())


# Concatenacion de STRINGS
first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())