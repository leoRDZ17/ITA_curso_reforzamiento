# Tomar datos
print("Ingrese peso en kg:")
peso = float(input())
print("Ingrese altura en m:")
altura = float(input())

# Calcular e imprimir IMC
imc = peso / (altura ** 2)
print("IMC es: ", imc)