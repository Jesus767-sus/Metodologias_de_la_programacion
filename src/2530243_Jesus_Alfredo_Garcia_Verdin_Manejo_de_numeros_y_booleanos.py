# Nombre: Jesus Alfredo Garcia Verdin Matricula: 2530243 
# Carrera de Ingenieria en mecatronica
# Grupo 1:3
# Manejo de listas tupplas y diccionarios en python
# Profesor: Carlos Antonio Tovar Garcia.

"""
Este proyecto reúne siete programas desarrollados en Python que se centran en el manejo 
de datos numéricos, valores lógicos y el procesamiento de cadenas de texto. Cada ejercicio 
incorpora validaciones de entrada, uso de condiciones, control de errores y un formato adecuado 
de salida para garantizar resultados ordenados y comprensibles.

Las actividades presentan aplicaciones reales del uso de números enteros y decimales en 
operaciones matemáticas, el tratamiento de textos mediante métodos de cadenas y la evaluación 
de expresiones booleanas en la toma de decisiones. Estos conocimientos se aplican en situaciones 
prácticas como conversiones, comparaciones, organización de información y análisis de datos 
ingresados por el usuario.

Además, el proyecto fortalece competencias fundamentales en programación, como la creación 
de algoritmos, la correcta definición de entradas y salidas, el uso de casos de prueba y la 
validación de datos para prevenir errores. En conjunto, este trabajo contribuye a una mejor 
comprensión del funcionamiento de Python en el manejo de datos, cálculos y decisiones lógicas 
dentro de programas bien estructurados y confiables.
"""


# Problem 1: Temperature Converter
"""
Description:
Converts from degrees Celsius to Fahrenheit using user input.

Inputs:
- temp_c: number

Outputs:
- Fahrenheit temperature

Validations:
- Input must be numeric.

Test cases:
1) Normal: 0 -> 32
2) Borded: 25 -> 77
3) Error: "abc" -> Error
"""

temp_c = input("Enter Celsius: ").strip()
try:
    c = float(temp_c)
    f = (c * 9/5) + 32
    print(f"Fahrenheit: {f}")
except:
    print("Error")


# Problem 2: Extra Hours Salary Calculator
"""
Description:
Determines the salary based on the hours worked and the cost per hour, considering 
additional payment for overtime hours greater than 40.

Inputs:
- hours: number
- rate: number

Outputs:
- Total salary

Validations:
- Both inputs must be numeric and positive.

Test cases:
1) Normal: hours=40, rate=10 -> 400
2) Borded: hours=45, rate=10 -> 475
3) Error: hours="abc" -> Error
"""

hours = input("Hours worked: ").strip()
rate = input("Hourly rate: ").strip()
try:
    h = float(hours)
    r = float(rate)
    if h < 0 or r < 0:
        print("Error")
    else:
        if h > 40:
            total = (40*r) + ((h-40)*(1.5*r))
        else:
            total = h*r
        print(total)
except:
    print("Error")


# Problem 3: Discount Evaluator
"""
Description:
Determines the final cost of a product after applying the discount according to the indicated quantity.

Inputs:
- amount: number

Outputs:
- Final price with discount

Validations:
- Amount must be numeric and >= 0.

Test cases:
1) Normal: 100 -> no discount
2) Borded: 600 -> 10% discount
3) Error: "abc" -> Error
"""

amount = input("Amount: ").strip()
try:
    a = float(amount)
    if a < 0:
        print("Error")
    else:
        if a >= 500:
            final_price = a * 0.90
        else:
            final_price = a
        print(final_price)
except:
    print("Error")


# Problem 4: Integer Stats
"""
Description:
Analyzes three integers to obtain the lowest, highest, and corresponding average value.

Inputs:
- n1, n2, n3: integers

Outputs:
- Minimum, maximum, average

Validations:
- All inputs must be integers.

Test cases:
1) Normal: 1, 5, 10 -> min=1, max=10, avg=5.33
2) Borded:-3, 0, 3 -> min=-3, max=3, avg=0
3) Error: "a", 5, 9 -> Error
"""

n1 = input("Enter integer 1: ").strip()
n2 = input("Enter integer 2: ").strip()
n3 = input("Enter integer 3: ").strip()
try:
    i1 = int(n1)
    i2 = int(n2)
    i3 = int(n3)
    mn = min(i1, i2, i3)
    mx = max(i1, i2, i3)
    avg = (i1 + i2 + i3) / 3
    print(mn, mx, avg)
except:
    print("Error")


# Problem 5: Loan Eligibility Checker
"""
Description:
Analyzes whether a person meets the requirements based on their age and monthly income.

Inputs:
- age: number
- income: number

Outputs:
- eligible / not eligible

Validations:
- Age and income must be numeric and >= 0.

Test cases:
1) age=25, income=15000 -> eligible
2) age=17, income=20000 -> not eligible
3) "abc", 20000 -> Error
"""

age = input("Enter age: ").strip()
income = input("Enter income: ").strip()
try:
    ag = float(age)
    inc = float(income)
    if ag < 0 or inc < 0:
        print("Error")
    else:
        if ag >= 18 and inc >= 10000:
            print("eligible")
        else:
            print("not eligible")
except:
    print("Error")


# Problem 6: Product Label Formatter
"""
Description:
Build a label respecting an exact length of 30 characters.

Inputs:
- product_name: string
- price_value: number/string

Outputs:
- 30-character label

Validations:
- Name must not be empty.
- Price must be numeric and positive.

Test cases:
1) Normal: "Apple", 10 -> label (30 chars)
2) Borded: long name -> trimmed
3) Error: price="abc" -> Error
"""

product_name = input("Enter product name: ").strip()
price_value = input("Enter price: ").strip()

if product_name == "" or price_value == "":
    print("Error")
else:
    try:
        price_num = float(price_value)
        label = f"Product: {product_name} | Price: ${price_num}"
        if len(label) < 30:
            label = label + (" " * (30 - len(label)))
        else:
            label = label[:30]
        print(f"Label: \"{label}\"")
    except:
        print("Error")


# Problem 7: Password Strength Classifier
"""
Description:

Determines the security level of a password by taking into account its size and the 
variety of characters used.

Inputs:
- password_input: string

Outputs:
- weak / medium / strong

Validations:
- Must not be empty.

Test cases:
1) Normal: "Abc123!!" -> strong
2) Borded: "password" -> weak
3) Error: "" -> Error
"""

password_input = input("Enter password: ").strip()

if password_input == "":
    print("Error")
else:
    length = len(password_input)
    has_upper = any(c.isupper() for c in password_input)
    has_lower = any(c.islower() for c in password_input)
    has_digit = any(c.isdigit() for c in password_input)
    has_special = any(not c.isalnum() for c in password_input)

    score = 0
    if length >= 8:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score >= 3:
        print("strong")
    elif score == 2:
        print("medium")
    else:
        print("weak")


# Conclusiones
"""
En conclusión, el manejo de números y valores booleanos en Python es fundamental para el 
desarrollo de programas funcionales y confiables, ya que permite realizar cálculos precisos 
y tomar decisiones lógicas dentro del flujo del programa. A través del uso de enteros, flotantes
y expresiones booleanas, es posible resolver problemas reales como conversiones, comparaciones, 
evaluaciones de condiciones y control de procesos. La correcta aplicación de estos conceptos, 
junto con la validación de datos de entrada y el uso de estructuras condicionales, contribuye 
a la creación de programas más seguros, claros y eficientes. Dominar el tratamiento de números 
y booleanos fortalece la lógica de programación y sienta las bases para el desarrollo de aplicaciones 
más avanzadas en Python.
"""

# References
"""
1) Python Documentation – Built-in Types.
2) Python String Methods – Official Docs.
3) Real Python – Boolean Logic in Python.
4) W3Schools – Python Input and Data Types.
5) Automate the Boring Stuff with Python – Chapters on strings & logic.
"""
