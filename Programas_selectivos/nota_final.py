# Tomar datos para calcular nota final
parciales = float(input("Nota parciales: "))
proyecto = float(input("Nota proyecto: "))
examen = float(input("Nota examen: "))

# Asegurar que los datos estan en un rango de 0-100 y calcular nota final
if (parciales < 0 or parciales > 100) or (proyecto < 0 or proyecto > 100) or (examen < 0 or examen > 100):
    print("ERROR: Las notas deben estar en un rango de 0-100")
else:
    nota_final = (parciales * 0.4) + (proyecto * 0.3) + (examen * 0.3)
    print("Nota final: ", nota_final)