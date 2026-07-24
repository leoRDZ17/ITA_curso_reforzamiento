# Vocales / No vocales
while True:
    letra = input("Ingrese letra (espacio para salir): ")

    # Verificar si, debe terminar, si es vocal o no
    if letra == " ":
        break
    letra = letra.lower()
    if letra in "aeiou":
        print("Vocal")
    else:
        print("Consonante")
print("Programa finalizado")