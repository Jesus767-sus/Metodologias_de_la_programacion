# Nombre: Jesus Alfredo Garcia Verdin Matricula: 2530243 
# Carrera de Ingenieria en mecatronica
# Grupo 1:3
# Manejo de listas tupplas y diccionarios en python
# Profesor: Carlos Antonio Tovar Garcia.
"""
RESUMEN EJECUTIVO

Este proyecto se enfocó en la aplicación práctica de los bucles for y while en Python, 
los cuales son fundamentales para ejecutar tareas repetitivas de manera automática y eficiente. 
A través de los ejercicios se puso en práctica el recorrido de rangos, listas y cadenas, así 
como el uso de contadores, acumuladores y estructuras condicionales. También se destacó la 
importancia de validar correctamente las entradas, controlar la finalización de los ciclos y 
presentar adecuadamente los resultados. Mediante la resolución de problemas como cálculos 
iterativos, generación de patrones y procesamiento de datos, se fortaleció la capacidad para 
crear algoritmos bien estructurados, reforzando además la claridad, organización y precisión 
en la programación en Python.
"""

# 7.1 Problem 1: Sum of range with for
"""
Descripción:
What this job does is that it calculates the sum of all integers from 1 to n (including n). 
Additionally, it calculates the sum of only even numbers within the same range using a for loop.

Entries:
- n (int): upper limit of the range.

Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validations:
- n must be convertible to int.
- n >= 1; otherwise print "Error: invalid input".

Test cases:
1) Normal = 5 → Sum = 15, Even sum = 6
2) Borded = 10 → Sum = 55, Even sum = 30
3) Error = -2 → Error
"""

n_input = input("Enter n: ")

try:
    n = int(n_input)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0
        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except:
    print("Error: invalid input")


# 7.2 Problem 2: Multiplication table with for
"""
Descripción:
What this code does is that it generates the multiplication table of a base number, 
from 1 to m, using a for loop.

Entries:
- base (int)
- m (int): table limit.

Outputs:
- One line per multiplication: "<base> x <i> = <result>"

Validations:
- base and m must be convertible to int.
- m >= 1; otherwise print "Error: invalid input".

Test cases:
1) Normal: base=5, m=4 → prints 4 lines
2) Borded: base=9, m=10 → prints 10 lines
3) Error: base="aaa" → Error
"""

base_input = input("Enter base: ")
m_input = input("Enter m: ")

try:
    base = int(base_input)
    m = int(m_input)
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
except:
    print("Error: invalid input")


# 7.3 Problem 3: Average with while and sentinel
"""
Descripción:
What this code does is that it reads numbers one by one until the user enters the sentinel value (-1). 
Calculates the average and the number of numbers entered. If no valid value is entered, 
it displays error.

Entries:
- number (float) repeatedly
- sentinel = -1

Outputs:
- "Count:" <count>
- "Average:" <average>
- "Error: no data" if no valid input.

Validations:
- Each number must be convertible to float.
- Sentinel must not be included in calculations.

Test cases:
1) Normal:3, 6, 9, -1 → Count=3, Avg=6
2) Borded: 10, -1 → Count=1, Avg=10
3) Error: -1 → Error
"""

sentinel = -1
count = 0
total = 0.0

while True:
    value = input("Enter number (-1 to stop): ")
    try:
        num = float(value)
        if num == sentinel:
            break
        total += num
        count += 1
    except:
        print("Invalid number, ignored.")

if count == 0:
    print("Error: no data")
else:
    print("Count:", count)
    print("Average:", total / count)


# 7.4 Problem 4: Password attempts with while
"""
Descripción:
This job is a Password Verification System with a maximum number of attempts. 
If the password entered is correct before exhausting attempts, success is displayed. 
If the attempts are exhausted, the account is blocked.

Entries:
- user_password (string)

Outputs:
- "Login success" if correct
- "Account locked" if attempts exhausted

Validations:
- MAX_ATTEMPTS > 0
- Count attempts correctly

Test cases:
1) Normal: Correct on first try → success
2) Borded: Wrong, wrong, correct → success
3) Error: Empty input → attempts consumed
"""

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    pwd = input("Enter password: ")
    if pwd == CORRECT_PASSWORD:
        print("Login success")
        break
    else:
        attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")


# 7.5 Problem 5: Simple menu with while
"""
Descripción:
What this job does is that it creates an interactive menu that repeats until the user chooses 0 (exit). 
Includes a counter that can be viewed or incremented.

Entries:
- option (int)

Outputs:
- "Hello!"
- "Counter:" <value>
- "Counter incremented"
- "Bye!"
- "Error: invalid option"

Validations:
- option must be convertible to int
- Only 0,1,2,3 valid

Test cases:
1)  Normal: 1 → Hello!
2) Borded: → increments counter
3) Error: → error
"""

counter = 0

while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    opt = input("Select option: ")

    try:
        opt = int(opt)
    except:
        print("Error: invalid option")
        continue

    if opt == 0:
        print("Bye!")
        break
    elif opt == 1:
        print("Hello!")
    elif opt == 2:
        print("Counter:", counter)
    elif opt == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")


# 7.6 Problem 6: Pattern printing with nested loops
"""
Descripción:
This code Prints a pattern of asterisks in the shape of a right triangle using nested for loops.
Optionally, an inverted triangle can also be printed.

Entries:
- n (int): number of rows for the pattern.

Outputs:
- Pattern printed line by line:
  *
  **
  ***
  ****

Validations:
- n must be convertible to int
- n >= 1

Test cases:
1) Normal: n=1 → "*"
2) Borded: n=5 → prints 5 lines
3) Error: n=0 → error
"""

n_input = input("Enter n: ")

try:
    n = int(n_input)
    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            print("*" * i)
except:
    print("Error: invalid input")


"""
CONCLUSIONES

En conclusión, el manejo de los bucles en Python, especialmente de las estructuras 
for y while, es fundamental para el desarrollo de programas eficientes y automatizados. 
Estas herramientas permiten repetir procesos de forma controlada, facilitar el recorrido 
de datos y optimizar el tiempo de ejecución al evitar instrucciones repetitivas. Un uso 
adecuado de los bucles, acompañado de validaciones y condiciones de salida correctas, garantiza 
programas más seguros, claros y libres de errores como los ciclos infinitos. El dominio de estas 
estructuras fortalece la lógica de programación del estudiante y representa una base 
indispensable para abordar problemas más complejos dentro del desarrollo de software en Python.
"""
# Repositorio en github:
"""
https://github.com/Jesus767-sus/Metodologias_de_la_programacion
"""
"""
REFERENCIAS

[1] M. Lutz, Learning Python, 5th ed. Sebastopol, CA, USA: O’Reilly Media, 2013.

[2] E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming,
2nd ed. San Francisco, CA, USA: No Starch Press, 2019.

[3] Python Software Foundation, "Python 3 Documentation". Disponible en:
https://docs.python.org/3/

[4] J. Zelle, Python Programming: An Introduction to Computer Science, 
3rd ed. Franklin, Beedle & Associates, 2016.

[5] D. Beazley and B. Jones, Python Cookbook, 3rd ed. Sebastopol, CA, USA:
O’Reilly Media, 2013.
"""
