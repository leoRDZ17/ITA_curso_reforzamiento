# Entrada de datos
mes = int(input("Numero de mes (1-12): "))

# Estaciones del año
match mes:
    case 12 | 1 | 2:
        estacion = "Invierno"
    case 3|4|5:
        estacion = "Primavera"
    case 6|7|8:
        estacion = "Verano"
    case 8|9|10|11:
        estacion = "Otoño"
    case _:
        estacion = "Mes invalido"

print("Estacion actual: ", estacion)