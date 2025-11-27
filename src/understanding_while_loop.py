# While
"""
El while es un ciclo controlado/comando por condicion
la estructura basica while es:
while conditional:
   actions
"""

# While infinito 
"""
Programa si el usuario escribe un numeros entre 25 y 50, entonces estar dentro del rango
y salirme del while, de otro modo pedirle otro numero.
"""
""""
Docsing for understanding_while_loop_centinel

- cuente cuantos numeros ha ingersado el usuario
-realise la suma de los numeros ingresados
-me diga cual es el minimo y el maximo de los numeros ingresados

"""
counter = 0
sum_quantities= 0.0
minimum = None
maximum = None  



while True:
    print("escribe exit para salir")
    user_imput = input("ingresa una cantidad (MXN): ")
    
    if user_imput == exit:
       break


    try:
        value = float(user_imput)
    except ValueError:
        print("ingresa un valor numerico valido")
        continue
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario")
        break    

counter = counter + 1
sum_quantities = sum_quantities + value 

if minimum is None or value < minimum:
    minimum = value

if maximum is None or value > maximum:
    maximum = value

print(f"cantidad de numeros ingresados: {counter}")
print(f"suma de los numeros ingresados: {sum_quantities}")  
print(f"el numero minimo es: {minimum}")
print(f"el numero maximo es: {maximum}")