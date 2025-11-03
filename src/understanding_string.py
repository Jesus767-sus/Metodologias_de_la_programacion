"""
String variables

Un string es de manera sencilla una serie de caracteres. 
En python, todo lo que se encuentre dentro de comillas simples o dobles
 sera considerado un string.

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

# Whitespaces
"""
Un whitspace se refiere a cualquier caracter que no se imprime, es decir
un espacio, tabuladores y finales de linea. Los whitespaces se utilizan 
comunmente para organizar las salidas de tal manera que sea mas 
amigable de leer o ver para el usuario.

Ejemplo:
-Tabulador: \t
-Salto de linea: \n
"""
print("Whitespace Tabulador")
print("Python")
print("\tPython")
print("\t\tPython")

print("Whitespace Salto de linea")
print("Languajes: \n\tPython\nC\n\tJavascript")

# Eliminacion de espacios en blanco
programming_languages = " Python "
print(programming_languages)
print(programming_languages.rstrip())
print(programming_languages.lstrip())
print(programming_languages.strip())

# Syntax error con string
message = "Una fortaleza de python es su comunidad"
print(message)
message = "Una fortaleza de python es su comunidad"
print(message)

# f-strings
famous_person = "Taylor Swift"
message = f"{famous_person} una vez dijo me voy al oxxo en avion"
print(message)

print(f"{famous_person.upper()} una vez dijo me voy al oxxo en avion.")

# Actividad
"""
Elije el nombre de una persona famosa (quien tu quieras).
Elije una cita famosa de esta persona.
Iguala ambos strings a una variable.

1) Realiza la concatenacion utilizando el signo de suma.
2) Realiza la concatenacion utilizando fstrings
"""

famous_person_upv = "Charly Mercury dijo"
quote_of_famous_person = "Python es el mejor lenguaje de programacion"
message = famous_person_upv + " " + quote_of_famous_person
print(famous_person_upv+ " " + quote_of_famous_person)
print(message)

f_string_message = f"{famous_person_upv} {quote_of_famous_person}"
print(f_string_message)

# Numbers 
"""
Enteros

Los podemos sumas (+), restar (-), multiplicar (*), divididir (/).
Les podemos aplicar potencias(**2, **3, **3), modulo (%)
"""

number_1 = 35
number_2 = 35
suma = number_1+number_2
resta = number_1-number_2
multiplicacion = number_1*number_2
division = number_1/number_2
potencia = number_1**2
modulo = number_1%number_2
print("Suma: ", suma, type(suma))
print("Resta: ", resta, type(resta))
print("Multiplicacion: ", multiplicacion, type(multiplicacion))
print("Division: ", division, type(division))
print("Potencia: ", potencia, type(potencia))
print("Modulo: ", modulo, type(modulo))

"""
Jerarquia de operaciones
2+3*4 -> 14
(2+3)*4 -> 20
"""

"""
Floats
Python llama floats a cualquier numero con punto decimal.
Los podemos sumas (+), restar (-), multiplicar (*), divididir (/).
Les podemos aplicar potencias(**2, **3, **3)
"""

print(0.1+0.1)
print(0.2-0.2)
print(0.1*2)
print(2*0.2)

# Imprimir la edad de alguien

age = 33 
message2 = "Charly tiene " + str(age) + " años."
print(message2)

"""
TypeError: Esto significa que python no puede reconicer el tipo de 
informacion que se esta utilizando.
"""