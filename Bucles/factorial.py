# Factorial
num = int(input("Numero para factorial: "))
factorial = 1

# Verificar que el num no es negativo y realizar opeeracion factorial
if num < factorial:
    print("Factorial no definido para negativos")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de ", num, " es: ", factorial)