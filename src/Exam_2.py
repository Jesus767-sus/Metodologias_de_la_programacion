# Jesus Alfredo Garcia Verdin 2530243
def area_perimetro_rectangulo(base, altura):
    if base <= 0 or altura <= 0:
        return "Error: La base y la altura deben ser mayores que cero."
    
    area = base * altura
    perimetro = 2 * (base + altura)
    
    return area, perimetro
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))
resultado = area_perimetro_rectangulo(base, altura)
if isinstance(resultado, str):
    print(resultado)
else:
    area, perimetro = resultado
    print(f"El área del rectángulo es: {area}")
    print(f"El perímetro del rectángulo es: {perimetro}")
