# Funcion que itera los elementos de la lista y los suma
def sumar_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

# Lista vacia
numeros = []

# Bucle de entrada de datos para la lista numeros
for i in range(5):
    valor = int(input(f"Ingrese numero {i+1}: "))
    numeros.append(valor)

# Uso de la funcion sumar_lista y de sum para sumar los elementos de la lista
total = sumar_lista(numeros)
total_sum = sum(numeros)

# Imprimir los resultados en pantalla
print("Suma con bucle: ", total)
print("Suma con sum(): ", total_sum)