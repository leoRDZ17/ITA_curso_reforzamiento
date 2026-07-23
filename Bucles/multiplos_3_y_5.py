# Multiplos de 3 y 5
print("Numeros divisibles por 3 y 5 (1-100):")

# Bucle
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")
print()