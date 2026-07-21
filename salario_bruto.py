salario = float(input("Salario bruto: "))
porcentaje = float(input("% Impuestos: "))
deducciones = float(input("Deducciones"))

impuesto = salario * (porcentaje / 100)
salario_net = salario-impuesto-deducciones

print("Salario neto: ", salario_net)