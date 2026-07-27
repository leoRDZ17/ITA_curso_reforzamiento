import math

def mcd(a,b):
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))

resultado = mcd(num1,num2)
resultado_m = math.gcd(num1,num2)

print("MCD Calculado: ", resultado)
print("MCD Calculado con math: ", resultado_m)
print("Los resultados coinciden" if resultado and resultado_m else "No coinciden")

if num1 == 0 and num2 == 0:
    print("Caso especial ambos son cero")
else:
    print("Programa terminado")