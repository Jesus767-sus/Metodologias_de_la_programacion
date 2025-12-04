# Usa las bubble sort para ordenar la lista list_origin = [7, 3, 9, 1, 4, 2]
def bubble_sort(list_origin):
    n = len(list_origin)
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if list_origin[j] > list_origin[j+1]:
                list_origin[j], list_origin[j+1] = list_origin[j+1], list_origin[j]
    return list_origin
list_origin = [7, 3, 9, 1, 4, 2]
sorted_list = bubble_sort(list_origin)
print(f"Lista original: {[7, 3, 9, 1, 4, 2]}")
print(f"Lista ordenada: {sorted_list}")


