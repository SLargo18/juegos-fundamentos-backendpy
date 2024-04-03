import random

opciones = ["piedra", "papel", "tijeras"]

def obtener_eleccion_computadora():
    return random.choice(opciones)

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (
        (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or
        (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or
        (eleccion_usuario == "tijeras" and eleccion_computadora == "papel")
    ):
        return "Usuario"
    else:
        return "Computadora"

def jugar():
    while True:
        eleccion_usuario = input("Elige piedra, papel o tijeras (o ingresa 'salir' para terminar): ")

        if eleccion_usuario == "salir":
            print(" nos vemos luego!")
            break

        if eleccion_usuario not in opciones:
            print("no te entiendo, intenta de nuevo.")
            continue

        eleccion_computadora = obtener_eleccion_computadora()
        print(f"Tú elegiste: {eleccion_usuario}")
        print(f"yo elegí: {eleccion_computadora}")

        ganador = determinar_ganador(eleccion_usuario, eleccion_computadora)
        if ganador == "Empate":
            print("empate")
        else:
            print(f"{ganador} gana esta ronda!")

jugar()