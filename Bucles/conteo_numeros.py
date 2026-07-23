# Conteo
n = int(input("Cantidad de numeros a ingresar: "))
mayores = 0
menores = 0
iguales = 0

# Bucle
for i in range(n):
    num = int(input("Numero: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

# Imprimir en pantalla
print("Mayores a 0: ", mayores)
print("Menores a 0: ", menores)
print("Iguales a 0: ", iguales)