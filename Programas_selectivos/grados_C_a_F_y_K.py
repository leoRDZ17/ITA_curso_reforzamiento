# Entrada de datos de grados Celsius y tipo de conversion
celsius = float(input("Ingrese los grados en Celsius: "))
print("Conversiones: 1.C a Farenheit 2. C a Kelvin")
opcion = int(input("Seleccione el tipo de conversion: "))

# Realizar el cambio en base al tipo de conversion seleccionado
match opcion:
    case 1:
        resultado = celsius * 9/5 + 32
        unidad = "°F"
    case 2:
        resultado = celsius + 273.15
        unidad = "°K"
    case _:
        resultado = None
        print("Opcion invalida")
if resultado is not None:
    print("Conversion: ", resultado, unidad)