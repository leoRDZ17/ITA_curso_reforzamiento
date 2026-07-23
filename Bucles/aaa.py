# Contar letras a en palabra
palabra = input("Ingrese la palabra: ").lower()
contador = 0

# Bucle
for letra in palabra:
    if letra == 'a':
        contador += 1
print("La letra 'a' aparece ", contador, " veces")