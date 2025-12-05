# Jesus Alfredo Garcia Verdin Matricula: 2530243 
# Carrera de Ingenieria en mecatronica
# Grupo 1:3
## Programa serie de fibonacci.

"""
La serie de Fibonacci es una sucesión de números donde cada número se obtiene al sumar los dos anteriores. 
Comienza con 0 y 1, formando la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21…

Significa generar y mostrar únicamente los primeros n números de la serie de Fibonacci, donde n es 
la cantidad de términos que el usuario desea obtener. Por ejemplo, si n = 5, se mostrarán los primeros cinco 
valores de la sucesión.
El programa realizará las siguientes acciones:
Lectura del valor n ingresado por el usuario.
Validación básica para asegurar que n sea un número válido.
Generación y presentación de la serie de Fibonacci hasta el número de términos indicado.
"""
"""
Problem: Fibonacci series generator  
Description: Program that reads an integer n and prints the first n terms of the Fibonacci series starting at 0 and 1.  

Inputs:  
- n (int; number of terms to generate)  

Outputs:  
6.1 Problem: Fibonacci series up to n terms

Descripción:
Implementa un programa que calcule y muestre la serie de Fibonacci hasta n términos, donde n es ingresado por el usuario. La serie debe comenzar en 0 y 1, por lo que:

- Si n = 1 → salida: 0  
- Si n = 2 → salida: 0, 1  
- Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8  

El programa debe:
1) Leer n desde la entrada estándar.  
2) Validar n.  
3) Generar la serie de Fibonacci con un bucle (for o while).  
4) Imprimir los términos en una sola línea, separados por espacios o comas.

Entradas:
- n (int; número de términos de la serie a generar).

Salidas:
- "Number of terms:" <n> (opcional)
- "Fibonacci series:" <term_1> <term_2> ... <term_n>

Validaciones:
- n debe poder convertirse a entero.
- n >= 1.
- (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
- Si la validación falla, NO calcular la serie.

Ejemplo de comportamiento esperado:
- Entrada: n = 5
- Salida:
  - Fibonacci series: 0 1 1 2 3

Validations:  
- n must be an integer  
- n must be >= 1  
- (Optional) n must be <= 50  

Test cases:  
1) Normal: n = 5 → expected series: 0 1 1 2 3  
2) Border: n = 1 → expected series: 0  
3) Error: n = -3 → expected message: "Error: invalid input"  
"""

# Lectura y validación del número de términos
while True:
    try:
        n = int(input("Number of terms: "))

        if n < 1 or n > 50:
            print("Error: invalid input")
            continue
        else:
            break

    except ValueError:
        print("Error: invalid input")

# Generación de la serie de Fibonacci
a, b = 0, 1
fibonacci = []

for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b

# Salida
print("Fibonacci series:", end=" ")
for num in fibonacci:
    print(num, end=" ")

# Conclucion
"""
El uso de un bucle facilitó la generación ordenada y eficiente de la serie de Fibonacci, ya que permitió 
calcular automáticamente cada término a partir de los anteriores sin necesidad de repetir instrucciones. 
Además, manejar correctamente los casos especiales cuando n = 1 y n = 2 es fundamental, porque estos valores 
establecen la base de la secuencia y evitan errores en la salida del programa. Finalmente, la lógica utilizada 
para generar la serie de Fibonacci puede reutilizarse en distintos programas, como aplicaciones matemáticas, 
simulaciones, análisis de datos y resolución de problemas que requieran el uso de sucesiones numéricas.
"""
# References:
# 1) Python Documentation – Control Flow Tools (for and while loops)
#    https://docs.python.org/3/tutorial/controlflow.html
# 2) GeeksforGeeks – Fibonacci Series in Python
#    https://www.geeksforgeeks.org/python-program-for-fibonacci-numbers/
# 3) W3Schools – Python For Loops
#    https://www.w3schools.com/python/python_for_loops.asp
# 4) Apuntes de clase de Programación / Lógica de Programación

"""
Repositorio de github:
https://github.com/Jesus767-sus/Metodologias_de_la_programacion
"""