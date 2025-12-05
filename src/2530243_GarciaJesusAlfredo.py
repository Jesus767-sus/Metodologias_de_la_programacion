# Jesus Alfredo Garcia Verdin Matricula: 2530243 
# Carrera de Ingenieria en mecatronica
# Grupo 1:3
# Manejo de funciones en python

"""
Una función en Python es un bloque de código reutilizable que permite organizar un programa en partes 
pequeñas, claras y fáciles de mantener.

Los parámetros son los datos que una función espera recibir en su definición, mientras que los argumentos 
son los valores reales que se envían cuando la función es llamada.

Separar la lógica en funciones reutilizables facilita el mantenimiento del código, reduce errores, evita 
duplicar instrucciones y mejora la organización del programa.

El valor de retorno permite que una función entregue un resultado que puede ser reutilizado en otros 
cálculos, almacenado en variables o validado, lo cual es mejor que solo imprimir resultados.

Este documento incluye la descripción de los problemas, el diseño de funciones, las entradas, salidas, validaciones 
y casos de prueba básicos.
"""

# Problem 1: Rectangle area and perimeter calculator
#
# Description:
# This program defines two functions to calculate the area and the perimeter
# of a rectangle. The main code defines test values, validates them, calls the
# functions, and prints the results.
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
#
# Validations:
# - width must be greater than 0
# - height must be greater than 0
# - If validation fails, show "Error: invalid input"
#
# Test cases:
# 1) Normal: width = 5, height = 3 → Area = 15, Perimeter = 16
# 2) Border: width = 0.1, height = 0.1 → Area = 0.01, Perimeter = 0.4
# 3) Error: width = -4, height = 2 → Error: invalid input

def calculate_area(width, height):
    """
    Calculates the area of a rectangle.
    Parameters:
        width (float): width of the rectangle
        height (float): height of the rectangle
    Returns:
        float: area of the rectangle
    """
    return width * height


def calculate_perimeter(width, height):
    """
    Calculates the perimeter of a rectangle.
    Parameters:
        width (float): width of the rectangle
        height (float): height of the rectangle
    Returns:
        float: perimeter of the rectangle
    """
    return 2 * (width + height)


def main():
    # Test values (Normal case)
    width = 5.0
    height = 3.0

    # Input validation
    if width <= 0 or height <= 0:
        print("Error: invalid input")
        return

    # Function calls
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    # Outputs
    print("Result:")
    print("Area:", round(area, 2))
    print("Perimeter:", round(perimeter, 2))


if __name__ == "__main__":
    main()
# Problem 2: Grade classification
#
# Description:
# This program defines a function that classifies a numeric score (0–100)
# into a letter grade (A, B, C, D, or F). The main code uses test values,
# validates the input, calls the function, and displays the result.
#
# Inputs:
# - score (int or float)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - score must be between 0 and 100 inclusive
# - If validation fails, show "Error: invalid input"
#
# Test cases:
# 1) Normal: score = 85 → Category: B
# 2) Border: score = 90 → Category: A
# 3) Error: score = 120 → Error: invalid input

def classify_grade(score):
    """
    Classifies a numeric score into a letter grade.
    Parameters:
        score (float or int): numeric grade between 0 and 100
    Returns:
        str: grade category ("A", "B", "C", "D", or "F")
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    # Test value (Normal case)
    score = 85

    # Input validation
    if score < 0 or score > 100:
        print("Error: invalid input")
        return

    # Function call
    category = classify_grade(score)

    # Outputs
    print("Result:")
    print("Score:", score)
    print("Category:", category)


if __name__ == "__main__":
    main()

# Problem 3: Numbers summary (min, max, average)
#
# Description:
# This program defines a function that receives a list of numbers and returns
# a dictionary with the minimum, maximum, and average values. The main code
# builds the list from a comma-separated string, validates the input, calls
# the function, and displays the results.
#
# Inputs:
# - numbers_text (string, e.g., "10,20,30")
# - Internally: numbers_list (list of float)
#
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
#
# Validations:
# - numbers_text must not be empty after strip()
# - The list must not be empty after conversion
# - All elements must be valid numbers
# - If any validation fails, show "Error: invalid input"
#
# Test cases:
# 1) Normal: "10,20,30" → Min: 10, Max: 30, Average: 20
# 2) Border: "5" → Min: 5, Max: 5, Average: 5
# 3) Error: "10,abc,30" → Error: invalid input

def summarize_numbers(numbers_list):
    """
    Returns a summary dictionary with min, max, and average values.
    Parameters:
        numbers_list (list of float): list of numeric values
    Returns:
        dict: {"min": min_value, "max": max_value, "average": avg_value}
    """
    minimum_value = min(numbers_list)
    maximum_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)

    return {
        "min": minimum_value,
        "max": maximum_value,
        "average": average_value
    }


def main():
    # Test input (Normal case)
    numbers_text = "10,20,30"

    # Validation: empty text
    if not numbers_text.strip():
        print("Error: invalid input")
        return

    parts = numbers_text.split(",")
    numbers_list = []

    # Conversion and validation
    try:
        for value in parts:
            numbers_list.append(float(value.strip()))
    except ValueError:
        print("Error: invalid input")
        return

    # Validation: empty list after conversion
    if len(numbers_list) == 0:
        print("Error: invalid input")
        return

    # Function call
    summary = summarize_numbers(numbers_list)

    # Outputs
    print("Result:")
    print("Min:", summary["min"])
    print("Max:", summary["max"])
    print("Average:", round(summary["average"], 2))


if __name__ == "__main__":
    main()

# Problem 4: Apply discount list (pure function)
#
# Description:
# This program defines a pure function that receives a list of prices and a
# discount rate, and returns a NEW list with the discounted prices. The main
# code builds the list from a comma-separated string, validates the input,
# calls the function, and displays both the original and discounted lists.
#
# Inputs:
# - prices_text (string, e.g., "100,200,300")
# - discount_rate (float, between 0 and 1)
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
#
# Validations:
# - prices_text must not be empty after strip()
# - The converted list must not be empty
# - All prices must be greater than 0
# - 0 <= discount_rate <= 1
# - If any validation fails, show "Error: invalid input"
#
# Test cases:
# 1) Normal: "100,200,300", discount_rate = 0.10 → [90, 180, 270]
# 2) Border: "50", discount_rate = 0 → [50]
# 3) Error: "100,200", discount_rate = 1.5 → Error: invalid input

def apply_discount(prices_list, discount_rate):
    """
    Applies a discount to a list of prices and returns a new discounted list.
    This is a pure function: it does NOT modify the original list.
    Parameters:
        prices_list (list of float): list of original prices
        discount_rate (float): discount rate between 0 and 1
    Returns:
        list of float: new list with discounted prices
    """
    discounted_list = []

    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_list.append(discounted_price)

    return discounted_list


def main():
    # Test inputs (Normal case)
    prices_text = "100,200,300"
    discount_rate = 0.10

    # Validation: empty text
    if not prices_text.strip():
        print("Error: invalid input")
        return

    parts = prices_text.split(",")
    prices_list = []

    # Conversion and validation of prices
    try:
        for value in parts:
            price = float(value.strip())
            if price <= 0:
                print("Error: invalid input")
                return
            prices_list.append(price)
    except ValueError:
        print("Error: invalid input")
        return

    # Validation: empty list after conversion
    if len(prices_list) == 0:
        print("Error: invalid input")
        return

    # Validation: discount rate range
    if discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
        return

    # Function call
    discounted_prices = apply_discount(prices_list, discount_rate)

    # Outputs
    print("Result:")
    print("Original prices:", prices_list)
    print("Discounted prices:", [round(price, 2) for price in discounted_prices])


if __name__ == "__main__":
    main()

# Problem 5: Greeting function with default parameters
#
# Description:
# This program defines a function that builds a greeting message using a name
# and an optional title. If the title is provided, it is placed before the name.
# The main code calls the function using both positional and named arguments.
#
# Inputs:
# - name (string)
# - title (string, optional)
#
# Outputs:
# - "Greeting:" <greeting_message>
#
# Validations:
# - name must not be empty after strip()
# - title may be empty, but if provided, it is normalized using strip()
# - If name is invalid, show "Error: invalid input"
#
# Test cases:
# 1) Normal: name = "Alice", title = "Dr." → "Hello, Dr. Alice!"
# 2) Border: name = "Bob", title = "" → "Hello, Bob!"
# 3) Error: name = "" → Error: invalid input

def greet(name, title=""):
    """
    Builds a greeting message using a name and an optional title.
    Parameters:
        name (string): person's name
        title (string, optional): title to prepend to the name
    Returns:
        string: greeting message
    """
    clean_name = name.strip()
    clean_title = title.strip()

    if clean_title:
        full_name = clean_title + " " + clean_name
    else:
        full_name = clean_name

    return f"Hello, {full_name}!"


def main():
    # Test inputs (Normal case using named arguments)
    name = "Alice"
    title = "Dr."

    # Validation: name must not be empty
    if not name.strip():
        print("Error: invalid input")
        return

    # Function call using named arguments
    greeting_message = greet(name=name, title=title)

    # Output
    print("Result:")
    print("Greeting:", greeting_message)

    # Additional test (Border case using positional arguments)
    name_border = "Bob"
    title_border = ""

    if not name_border.strip():
        print("Error: invalid input")
        return

    greeting_border = greet(name_border, title_border)
    print("Greeting:", greeting_border)


if __name__ == "__main__":
    main()

# Problem 6: Factorial function (iterative implementation)
#
# Description:
# This program defines a function that calculates the factorial of a
# non-negative integer using an ITERATIVE approach (for loop).
# The main code defines a test value, validates it, calls the function,
# and displays the result.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be an integer
# - n must be greater than or equal to 0
# - n must be less than or equal to 20 (to avoid very large numbers)
# - If any validation fails, show "Error: invalid input"
#
# Test cases:
# 1) Normal: n = 5 → Factorial: 120
# 2) Border: n = 0 → Factorial: 1
# 3) Error: n = -3 → Error: invalid input

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using an iterative approach.
    Parameters:
        n (int): non-negative integer
    Returns:
        int: factorial value of n
    """
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def main():
    # Test input (Normal case)
    n = 5

    # Validation: must be integer
    if not isinstance(n, int):
        print("Error: invalid input")
        return

    # Validation: range check
    if n < 0 or n > 20:
        print("Error: invalid input")
        return

    # Function call
    factorial_value = factorial(n)

    # Outputs
    print("Result:")
    print("n:", n)
    print("Factorial:", factorial_value)


if __name__ == "__main__":
    main()

"""
CONCLUSION:
El uso de return fue más útil que solo imprimir, ya que los valores devueltos pudieron reutilizarse en otros 
cálculos y validaciones.

Los parámetros y valores por defecto hicieron las funciones más flexibles, permitiendo adaptarlas a diferentes 
situaciones sin cambiar su estructura.

Encapsular la lógica en funciones resultó especialmente útil en cálculos repetidos y validaciones, reduciendo 
errores y mejorando la claridad del programa.

Se aprendió a diferenciar entre la lógica principal, que controla el flujo del programa, y las funciones de 
apoyo, que realizan el procesamiento específico de datos.
"""
# References:
# 1) Python Documentation – Defining Functions (def, return, parameters)
# 2) Python Documentation – Data Structures (lists and dictionaries)
# 3) Real Python – Python Functions and Best Practices
# 4) GeeksforGeeks – Python Functions and Scope of Variables
# 5) Introduction to Algorithms and Programming – Basic Programming Concepts (Textbook/Notes)
# 6) Official Python Tutorial – Control Flow and Function Design
# 7) Class notes and official course resources on Python programming

"""
Repositorio en github:
https://github.com/Jesus767-sus/Metodologias_de_la_programacion
"""
