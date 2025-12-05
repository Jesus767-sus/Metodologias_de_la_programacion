# Jesus Alfredo Garcia Verdin Matricula: 2530243 
# Carrera de Ingenieria en mecatronica
# Grupo 1:3
# Trabajo de CRUD

"""
RESUMEN EJECUTIVO
Un CRUD es un conjunto de operaciones básicas que permiten la gestión de datos en un sistema. Sus siglas 
significan Create (Crear), Read (Leer), Update (Actualizar) y Delete (Eliminar), y representan las acciones 
}fundamentales para administrar información en aplicaciones, bases de datos y sistemas informáticos. Estas 
operaciones permiten registrar nuevos datos, consultarlos, modificarlos y eliminarlos de manera eficiente.

Para el desarrollo del programa se eligió como estructura de datos un diccionario o una lista de diccionarios,
ya que esta opción permite almacenar múltiples registros de forma organizada, asociando cada dato a una clave específica. Esta estructura facilita la búsqueda, actualización y eliminación de información, además de ser clara, flexible y adecuada para simular el funcionamiento de una base de datos en memoria.

El uso de funciones es esencial para organizar la lógica del CRUD, ya que permite separar cada operación 
(crear, leer, actualizar y eliminar) en módulos independientes. Esto mejora la legibilidad del código, facilita 
su mantenimiento, evita la repetición de instrucciones y permite reutilizar la lógica en otros programas de forma 
más eficiente.

El programa desarrollado cubre todas las funcionalidades básicas de un sistema CRUD, incluyendo un menú principal 
para que el usuario seleccione la operación a realizar, así como las funciones de creación de registros, lectura 
de datos, actualización, eliminación y listado de elementos. De esta manera, se garantiza una gestión completa de 
la información de forma estructurada, segura y fácil de usar para el usuario.
"""

"""
Problem: In-memory CRUD manager with functions
Descripción:
Programa que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) simple
para elementos almacenados en un diccionario, usando funciones para cada
operación y un menú de texto para interactuar con el usuario.

Inputs:
User menu options (string o int).
For CREATE/UPDATE: item_id, name, price, quantity.
For READ/DELETE: item_id.

Outputs:
Messages indicating the result of each operation:
"Item created"
Item updated"
"Item deleted"
"Item not found"
"Items list:", etc.

Validations:
Menu option must be valid (0..5).
item_id must not be empty.
Numeric fields must be valid numbers and >= 0.
Disallow creating an item with an id that is already in use.
For READ/UPDATE/DELETE, if the id does not exist, show "Item not found".

Test cases:
1) Normal: create an item, read it, update it, delete it → expected messages
and final empty list.
2) Border: create item with quantity = 0 and price = 0.
3) Error: invalid menu option, empty id, or non-numeric price.
"""
def create_item(items, item_id, name, price, quantity):
    if item_id in items:
        return False
    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(items, item_id):
    return items.get(item_id, None)


def update_item(items, item_id, new_name, new_price, new_quantity):
    if item_id not in items:
        return False
    items[item_id]["name"] = new_name
    items[item_id]["price"] = new_price
    items[item_id]["quantity"] = new_quantity
    return True


def delete_item(items, item_id):
    if item_id not in items:
        return False
    del items[item_id]
    return True


def list_items(items):
    if not items:
        print("No items registered.")
        return
    print("\nItems list:")
    for item_id, data in items.items():
        print(f"ID: {item_id} | Name: {data['name']} | Price: {data['price']} | Quantity: {data['quantity']}")


def valid_number(value, is_float=True):
    try:
        if is_float:
            num = float(value)
        else:
            num = int(value)
        return num >= 0
    except:
        return False


def main():
    items = {}

    while True:
        print("\n--- CRUD MENU ---")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")

        option = input("Choose an option: ").strip()

        if option not in ["0", "1", "2", "3", "4", "5"]:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        if option == "1":  # CREATE
            item_id = input("Enter id: ").strip()
            name = input("Enter name: ").strip()
            price = input("Enter price: ").strip()
            quantity = input("Enter quantity: ").strip()

            if not item_id or not valid_number(price, True) or not valid_number(quantity, False):
                print("Error: invalid input")
                continue

            if create_item(items, item_id, name, float(price), int(quantity)):
                print("Item created")
            else:
                print("Error: Item already exists")

        elif option == "2":  # READ
            item_id = input("Enter id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            item = read_item(items, item_id)
            if item:
                print(f"ID: {item_id} | Name: {item['name']} | Price: {item['price']} | Quantity: {item['quantity']}")
            else:
                print("Item not found")

        elif option == "3":  # UPDATE
            item_id = input("Enter id: ").strip()
            name = input("Enter new name: ").strip()
            price = input("Enter new price: ").strip()
            quantity = input("Enter new quantity: ").strip()

            if not item_id or not valid_number(price, True) or not valid_number(quantity, False):
                print("Error: invalid input")
                continue

            if update_item(items, item_id, name, float(price), int(quantity)):
                print("Item updated")
            else:
                print("Item not found")

        elif option == "4":  # DELETE
            item_id = input("Enter id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        elif option == "5":  # LIST
            list_items(items)


if __name__ == "__main__":
    main()

"""
CONCLUSIÓN
El uso de funciones permitió organizar mejor el programa, facilitando su comprensión, mantenimiento y 
reutilización del código para cada operación del CRUD.

El empleo de un diccionario para almacenar los datos ofreció ventajas como el acceso rápido a los ítems mediante 
su id, evitar duplicados y simplificar las operaciones de búsqueda, actualización y eliminación.

Uno de los principales retos fue la validación de las entradas, ya que se debían controlar opciones inválidas, 
valores no numéricos y campos vacíos. Esto se resolvió mediante verificaciones previas y el uso de try/except.

Este CRUD puede ampliarse a sistemas más grandes agregando almacenamiento en archivos (JSON, CSV) o conectándolo 
a bases de datos, además de poder adaptarse a interfaces gráficas o aplicaciones web.
"""
# References:
# 1) Python Documentation – Data Structures (dict, list):
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 2) Python Documentation – Defining Functions:
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 3) Real Python – CRUD Operations with Python:
#    https://realpython.com/python-crud/
#
# 4) GeeksforGeeks – CRUD Operations in Python:
#    https://www.geeksforgeeks.org/crud-operations-in-python/

"""
Repositorio en github:
https://github.com/Jesus767-sus/Metodologias_de_la_programacion
"""