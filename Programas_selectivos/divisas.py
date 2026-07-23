# Tomar datos para saber la cantidad y a que divisa convertir
cantidad = float(input("Ingrese la cantidad a convertir (MXN): "))
print("Divisas: 1.USD 2.EUR 3.THB 4.JPY 5KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
opcion = int(input("Seleccione opcion: "))

# Convertir la cantidad a la divisa seleccionada segun el caso de la variable opcion
match opcion:
    case 1:
        resultado = cantidad / 16.5
        moneda = "USD"
    case 2:
        resultado = cantidad / 18.0
        moneda = "EUR"
    case 3:
        resultado = cantidad / 0.45
        moneda = "THB"
    case 4:
        resultado = cantidad / 0.12
        moneda = "JPY"
    case 5:
        resultado = cantidad / 0.013
        moneda = "KRW"
    case 6:
        resultado = cantidad / 11.5
        moneda = "AUD"
    case 7:
        resultado = cantidad / 2.8
        moneda = "PEN"
    case 8:
        resultado = cantidad / 8.2
        moneda = "CAD"
    case 9:
        resultado = cantidad / 0.0023
        moneda = "VES"
    case 10:
        resultado = cantidad / 0.046
        moneda = "ARS"
    case _:
        print("Ingrese una opcion valida")
        resultado = None       
print("Conversion: ", resultado, moneda) 