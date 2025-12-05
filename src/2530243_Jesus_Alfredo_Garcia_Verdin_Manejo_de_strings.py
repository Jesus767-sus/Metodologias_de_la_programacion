# Nombre: Jesus Alfredo Garcia Verdin Matricula: 2530243 
# Carrera de Ingenieria en mecatronica
# Grupo 1:3
# Manejo de listas tupplas y diccionarios en python
# Profesor: Carlos Antonio Tovar Garcia.

"""
Este proyecto se enfoca en el manejo práctico de las cadenas de texto en Python a través 
de seis ejercicios diseñados para simular problemáticas reales. En cada actividad, el usuario
proporciona información que debe ser revisada, limpiada y transformada antes de ser 
utilizada por el programa, lo que permite reforzar la importancia del correcto tratamiento de 
los datos de entrada. Los problemas desarrollados incluyen el formateo de nombres completos, 
la validación básica de correos electrónicos, la detección de palíndromos sin considerar 
espacios, el análisis de palabras dentro de una oración, la clasificación de contraseñas según 
su nivel de seguridad y la creación de etiquetas de producto con un formato específico.

Para resolver cada ejercicio se aplican diversos métodos propios de los strings, como 
la eliminación de espacios innecesarios, el cambio entre mayúsculas y minúsculas, la sustitución 
de caracteres, el uso de separadores, el corte de cadenas y el conteo de elementos. Todo esto 
permite obtener versiones más limpias y organizadas del texto original. En conjunto, el proyecto 
resalta la importancia de normalizar y validar correctamente la información, fortalecer 
la lógica de programación y desarrollar habilidades esenciales para construir aplicaciones más 
confiables y seguras en Python.
"""

#Problem 1: Full name formatter

"""

Description:
Converts a full name to Title Case format and obtains the initials from the previously purified text.

Inputs:
- full_name: string

Outputs:
- Formatted name: <...>
- Initials: <...>

Validations:
- Input cannot be empty.
- Must contain at least two words.

Test cases:
1) Normal: "juan carlos tovar" -> Formatted name: Juan Carlos Tovar | Initials: J.C.T.
2) Border: "  ana   perez  " -> Ana Perez | A.P.
3) Error: "   " -> Error: invalid input
"""

full_name = input("Enter full name: ").strip()

if full_name == "" or len(full_name.split()) < 2:
    print("Error: invalid input")
else:
    parts = full_name.lower().split()
    formatted = " ".join([p.title() for p in parts])
    initials = ".".join([p[0].upper() for p in parts]) + "."
    print(f"Formatted name: {formatted}")
    print(f"Initials: {initials}")


#Problem 2: Simple email validator


"""
Description:
Validates that the email has only one '@', has no blank spaces and has at least one '.' 
in the part after the '@'.
Inputs:
- email_text: string

Outputs:
- Valid email: true/false
- Domain: <...> (if valid)

Validations:
- Email cannot be empty.
- Must have exactly one '@'.
- No spaces allowed.

Test cases:
1) Normal: "user@mail.com" -> Valid email: true | Domain: mail.com
2) Border: "test@domain" -> Valid email: false
3) Error: "user@@mail.com" -> Valid email: false
"""

email_text = input("Enter email: ").strip()

if email_text == "" or " " in email_text or email_text.count("@") != 1:
    print("Valid email: false")
else:
    at_index = email_text.find("@")
    domain = email_text[at_index + 1:]
    if "." in domain:
        print("Valid email: true")
        print(f"Domain: {domain}")
    else:
        print("Valid email: false")

#Problem 3: Palindrome checker

"""
Description:
Checks whether a sentence reads the same from front to back, ignoring spaces 
and differences between upper and lower case.

Inputs:
- phrase: string

Outputs:
- Is palindrome: true/false

Validations:
- Input cannot be empty.
- Minimum length after cleaning: 3 characters.

Test cases:
1) Normal: "Anita lava la tina" -> true
2) Border: "ala" -> true
3) Error: "a" -> Error: too short
"""

phrase = input("Enter phrase: ").strip()

if phrase == "":
    print("Error: invalid input")
else:
    cleaned = phrase.replace(" ", "").lower()
    if len(cleaned) < 3:
        print("Error: too short")
    else:
        is_pal = cleaned == cleaned[::-1]
        print(f"Is palindrome: {str(is_pal).lower()}")


#Problem 4: Sentence word stats

"""
Description:
Processes a sentence by displaying the total number of words along with the first, 
last, shortest, and longest.

Inputs:
- sentence: string

Outputs:
- Word count
- First word
- Last word
- Shortest and longest words

Validations:
- Cannot be empty.
- Must contain at least one valid word.

Test cases:
1) Normal: "hello world from python" -> count=4, first=hello, last=python
2) Border: "   hi   " -> count=1
3) Error: "    " -> Error: invalid input
"""

sentence = input("Enter sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    words = sentence.split()
    if len(words) == 0:
        print("Error: invalid input")
    else:
        shortest = min(words, key=len)
        longest = max(words, key=len)
        print(f"Word count: {len(words)}")
        print(f"First word: {words[0]}")
        print(f"Last word: {words[-1]}")
        print(f"Shortest word: {shortest}")
        print(f"Longest word: {longest}")


#Problem 5: Password strength classifier

"""
Description:
Determines the level of security of a password based on its length and diversity of symbols.

Inputs:
- password_input: string

Outputs:
- Password strength: weak/medium/strong

Validations:
- Cannot be empty.
- Length must be checked.

Test cases:
1) Normal: "Abc123!!" -> strong
2) Border: "password" -> weak
3) Error: "" -> Error: invalid input
"""

password_input = input("Enter password: ")

if password_input.strip() == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for c in password_input:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif not c.isalnum():
            has_symbol = True

    length = len(password_input)

    if length < 8 or (has_lower and not has_upper and not has_digit and not has_symbol):
        print("Password strength: weak")
    elif length >= 8 and ((has_upper and has_lower) or has_digit):
        if has_upper and has_lower and has_digit and has_symbol:
            print("Password strength: strong")
        else:
            print("Password strength: medium")
    else:
        print("Password strength: weak")

#Problem 6: Product label formatter

"""
Description:
Produces a label with length set to 30 characters, filling in or reducing the text 
to comply with the format.

Inputs:
- product_name: string
- price_value: string/number

Outputs:
- Label: "<30 char string>"

Validations:
- product_name cannot be empty.
- price_value must be numeric and positive.

Test cases:
1) Normal: product="Apple", price="10" -> valid label 30 chars
2) Border: long product name -> trimmed
3) Error: price="abc" -> invalid price
"""

product_name = input("Enter product name: ").strip()
price_value = input("Enter price: ").strip()

if product_name == "" or price_value == "":
    print("Error: invalid input")
else:
    try:
        price_num = float(price_value)
        label = f"Product: {product_name} | Price: ${price_num}"
        if len(label) < 30:
            label = label + " " * (30 - len(label))
        else:
            label = label[:30]
        print(f"Label: \"{label}\"")
    except:
        print("Error: invalid price")


"""
En conclusión, el manejo de strings en Python es una de las habilidades más importantes 
dentro de la programación, ya que permite trabajar de forma eficiente con la información 
textual que el usuario proporciona. A través de las distintas operaciones como limpieza, 
validación, transformación, análisis y formateo de cadenas, se logra que los programas sean más 
confiables, claros y seguros. El uso adecuado de métodos para modificar, comparar y extraer partes 
de un string facilita la solución de problemas reales como el procesamiento de nombres, correos, 
contraseñas y etiquetas. Dominar el manejo de cadenas fortalece la lógica de programación y sienta 
una base sólida para el desarrollo de aplicaciones más completas y profesionales en Python.
"""
# Repositorio en github:
"""
https://github.com/Jesus767-sus/Metodologias_de_la_programacion
"""
"""
References:
1) Python Documentation  Built-in Types: Text Sequence Type — str.
2) Python Official Tutorial  String Methods and Operations.
3) “Automate the Boring Stuff with Python”  Al Sweigart, Chapter on Strings.
4) Real Python  “Essential String Manipulation Techniques”.
5) W3Schools  Python String Methods Reference.
"""