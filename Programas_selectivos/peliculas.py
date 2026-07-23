# Entrada de datos
consulta = input("Ingrese nombre de la pelicula o serie: ").lower()

# Verificacion de casos
match consulta:
    case "inception":
        info = "Pelicula de ciencia ficcion de Christopher Nolan."
    case "the rolling stones":
        info = "Banda britanica de Londres"
    case "iron man":
        info = "Pelicula del mcu que rescato el genero de superheroes"
    case "spider-man":
        info = "Uno de los personajes mas influyentes del comic americano"
    case "stranger things":
        info = "Serie de terror y ciencia ficcion de Netflix"
    case _:
        info = "No hay informacion disponible"
print(info)