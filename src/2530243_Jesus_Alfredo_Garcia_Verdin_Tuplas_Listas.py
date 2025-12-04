# Nombre: Jesus Alfredo Garcia Verdin Matricula: 2530243 
# Carrera de Ingenieria en mecatronica
# Grupo 1:3
# Manejo de listas tupplas y diccionarios en python
# Profesor: Carlos Antonio Tovar Garcia.
"""
RESUMEN EJECUTIVO

Las listas y tuplas en Python son estructuras de datos para almacenar colecciones 
ordenadas de elementos, pero la principal diferencia es que las listas son mutables 
(se pueden modificar) y las tuplas son inmutables (no se pueden modificar una vez creadas). 
Las listas se definen con corchetes ``, mientras que las tuplas usan paréntesis (). 

Los diccionarios en Python son colecciones mutables y desordenadas de pares clave-valor, donde 
cada clave debe ser única e inmutable (como cadenas o números) para acceder a su valor 
correspondiente. Se definen usando llaves {} y se accede a los elementos usando la clave 
dentro de corchetes [], de manera similar a como se busca una palabra en un diccionario real 
para encontrar su definición. 

En este documento se veran 6 problemas a resolver en el cual se utilizaran, listas, tuplas y 
diccionarios con el motivo de que los alumnos aprendan a manejar mejor este tipo de datos en python.
Se estaran viendo varios casos de prueba para cada problema, y la mayor parte se estara resolviendo
sin el uso de copilot o chatGPT para asi mejorar el aprendizaje de los alumnos.
"""
# Problem 1 – Shopping List Basics
"""
DESCRIPTION:
In this program an initial list of products is created in which you can add a new 
product and at the last count the total items in the list and check if a specific 
product is in the list.

Entradas:
- initial_items_text (string)
- new_item (string)
- search_item (string)

Salidas:
- Items list
- Total items count
- Boolean value showing if item was found

Validaciones:
- initial_items_text must not be empty
- All items must be cleaned using strip()
- new_item and search_item must not be empty

Casos de prueba:
1) Normal: "apple,banana", "orange", "banana"
2) Border: "", "apple", "apple"
3) Error: "apple,banana", "orange", ""
"""

initial_items_text = "apple,banana,orange"
new_item = "grape"
search_item = "banana"

if initial_items_text.strip() == "":
    items_list = []
else:
    items_list = [i.strip() for i in initial_items_text.split(",")]

if new_item.strip() != "":
    items_list.append(new_item.strip())

is_in_list = search_item.strip() in items_list if search_item.strip() else False

print("Items list:", items_list)
print("Total items:", len(items_list))
print("Found item:", is_in_list)

# Problem 2 – Points and Distances with Tuples
"""
DESCRIPTION:
In this program, two tuples are created in which the Euclidean distance of those 
two points is seen and a midpoint tuple is created with the midpoint between them.

INPUTS:
- x1, y1, x2, y2 (float)

OUTPUTS:
- Point A, Point B
- Distance between points
- Midpoint tuple

VALIDATIONS:
- Inputs must be convertible to float

TEST CASES:
1) Normal: (1,2) and (5,9)
2) Border: (-5,-5) and (5,5)
3) Error: x1 = "abc"
"""

x1 = 0.0
y1 = 0.0
x2 = 3.0
y2 = 4.0

point_a = (x1, y1)
point_b = (x2, y2)

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2)/2, (y1 + y2)/2)

print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", distance)
print("Midpoint:", midpoint)

# Problem 3 – Product Catalog Dictionary
"""
DESCRIPTION:
This job manages a small catalog of products using a dictionary.

INPUTS:
- product_name (string)
- quantity (int)

OUTPUTS:
- Unit price
- Quantity
- Total price
- Error if product does not exist

VALIDATIONS:
- quantity > 0
- product_name must not be empty
- product must exist in dictionary

TEST CASES:
1) Normal: "apple", 2
2) Border: product in dict but quantity = 1
3) Error: product does not exist
"""

product_prices = {"apple": 10.0, "banana": 7.5, "milk": 22.0}

product_name = "apple"
quantity = 3

if product_name.strip() == "" or quantity <= 0:
    print("Error: invalid input")
elif product_name not in product_prices:
    print("Error: product not found")
else:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)


# Problem 4 – Student Grades
"""
DESCRIPTION:
This program manages a group's grades using a dictionary to see if the student passes or fails.

INPUTS:
- student_name (string)

OUTPUTS:
- Grades list
- Average
- Passed boolean
- Error if student does not exist

VALIDATIONS:
- student_name must not be empty
- student must exist
- grades list must not be empty

TEST CASES:
1) Normal: "Alice"
2) Border: student has exactly 1 grade
3) Error: student does not exist
"""

grades = {
    "Alice": [90, 85, 88],
    "Bob": [70, 75, 72],
    "Carol": [60, 65, 55]
}

student_name = "Alice"

if student_name.strip() == "":
    print("Error: invalid input")
elif student_name not in grades:
    print("Error: student not found")
else:
    student_grades = grades[student_name]
    average = sum(student_grades) / len(student_grades)
    is_passed = average >= 70.0
    print("Grades:", student_grades)
    print("Average:", average)
    print("Passed:", is_passed)


# Problem 5 – Word Frequency Counter
"""
DESCRIPTION:
This work Counts the frequency of each word in a sentence using list + dictionary.

INPUTS:
- sentence (string)

OUTPUTS:
- Words list
- Frequency dictionary
- Most common word

VALIDATIONS:
- sentence must not be empty
- words list must not be empty

TEST CASES:
1) Normal: "hello world hello"
2) Border: "apple"
3) Error: ""
"""

sentence = "apple banana apple orange"

if sentence.strip() == "":
    print("Error: invalid input")
else:
    words_list = sentence.lower().split()
    freq = {}
    for w in words_list:
        freq[w] = freq.get(w, 0) + 1
    most_common = max(freq, key=freq.get)

    print("Words list:", words_list)
    print("Frequencies:", freq)
    print("Most common word:", most_common)

# Problem 6 – Contact Book CRUD
"""
DESCRIPTION:
In this code implemented Implements a contact book using a dictionary with ADD, 
SEARCH and DELETE actions.

INPUTS:
- action_text
- name
- phone (only for ADD)

OUTPUTS:
- Contact saved
- Phone found
- Contact deleted
- Error if not found

VALIDATIONS:
- action must be ADD, SEARCH or DELETE
- name must not be empty
- phone must not be empty when adding

TEST CASES:
1) ADD: ("ADD", "Alice", "12345")
2) SEARCH: ("SEARCH", "Alice")
3) DELETE: ("DELETE", "Alice")
4) Error: search non-existing name
"""

contacts = {"Bob": "777888999"}

action_text = "ADD".upper()
name = "Alice"
phone = "555222111"

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    if action_text == "ADD":
        if name.strip() == "" or phone.strip() == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")


"""
CONCLUSIONS

In this work it was possible to understand and effectively apply the use of lists, tuples 
and dictionaries in Python, which are fundamental data structures for the development of 
efficient programs. Through its implementation, we will see how lists allow collections of 
data to be stored and modified dynamically, tuples offer a secure alternative as they are immutable, 
and dictionaries facilitate the organization of information using key-value pairs. The proper 
use of these structures not only improves the organization and management of data, but also 
optimizes processes within a program, allowing clearer, orderly and more efficient solutions. 
Finally, this work contributed to strengthening basic programming knowledge and developing 
essential skills for future projects in Python.
"""

"""
REFERENCES

[1] M. Lutz, *Learning Python*, 5th ed. Sebastopol, CA, USA: O_Reilly Media, 2013.

[2] E. Matthes, *Python Crash Course: A Hands-On, Project-Based Introduction to Programming*,
2nd ed. San Francisco, CA, USA: No Starch Press, 2019.

[3] Python Software Foundation, “Python 3 Documentation,” python.org. 
Available: https://docs.python.org/3/

[4] J. Zelle, *Python Programming: An Introduction to Computer Science*, 
3rd ed. Franklin, Beedle & Associates, 2016.

[5] D. Beazley and B. Jones, *Python Cookbook*, 3rd ed. Sebastopol, CA, USA: O’Reilly Media, 2013.
"""

