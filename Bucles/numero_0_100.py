# Adivinar numero
import random

secreto = random.randint(1,100)

# Bucle
while True:
    intento = int(input("Adivina (1-100): "))

    # Verificar si acerto o no
    if intento < secreto:
        print("Demasiado bajo")
    elif intento > secreto:
        print("Demasiado alto")
    else:
        print("¡Correcto! Era ", secreto)
        break
print("Juego terminado. El numero era ", secreto)