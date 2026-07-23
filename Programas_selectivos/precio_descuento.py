# Tomar datos
precio = float(input("Ingrese precio original: "))

# Calcular descuento
if precio <= 100:
    descuento = 0
elif precio <= 200:
    descuento = 0.1
elif precio <= 500:
    descuento = 0.2
else:
    descuento = 0.25

# Aplicar descuento
precio_fin = precio - (precio * descuento)

# Imprimir precio final
print("Descuento aplicado: ",descuento,"\nPrecio final: ", precio_fin)