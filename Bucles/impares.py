# Contador de numeros impares
N = int(input("Numero positivo: "))
i = 1

# Bucle
while True:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

    if i > N:
        print("\nFin. Se mostraron los impares hasta ", N)
        break