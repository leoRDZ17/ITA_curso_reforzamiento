# Funcion que cuenta los pares e impares
def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

# Lista vacia para registrar los numeros.
numeros = []

# Entrada de datos
for i in range(10):
    num = int(input("Numero {}: ".format(i+1)))
    numeros.append(num)

# Imprimir los resultados en pantalla
p, i = contar_pares_impares(numeros)
print("Pares: ", p)
print("Impares: ", i)