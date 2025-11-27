"""
Vamos a realizar un programa que defina un PIN
para dar acceso a un usuario.

El usuario va a tener un maximo de intentos para colocar bien el pin.

Si el usuario sobrepasa este maximo de intentos
se le va a bloquear la cuenta y el acceso.
"""

CORRECT_PIN = "1328"
MAX_ATTEMPTS = 3
attempt = 0
reaming_attemps = MAX_ATTEMPTS

while attempt < MAX_ATTEMPTS:
    
    
    user_input = input("Ingresa tu PIN ")

    if user_input == CORRECT_PIN:
        print("Acceso concedido")
        break
    else:
        attempt+=1
        reamining_attemps = MAX_ATTEMPTS - attempt
        if reamining_attemps > 0:
            print("Ingresa un pin, no valido")
            print(f"Te quedan {reamining_attemps} intentos")
        else:
            print("Cuenta bloqueada. No sabes buscate otra carrera tal vez seas mejor.")