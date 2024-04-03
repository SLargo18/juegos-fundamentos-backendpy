import random


def adivina_numero_usuario():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 10.")

    while True:
        intento = int(input("primer intento: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"Wow lo lograste! Adivinaste el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("El número es mayor intenta de nuevo.")
        else:
            print("El número es menor intenta de nuevo.")

# La Computadora adivina el número
def adivina_numero_computadora():
    rango_inferior = 1
    rango_superior = 10
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Piensa en un número entre 1 y 100, y yo intentaré adivinarlo.")

    while True:
        intento = random.randint(rango_inferior, rango_superior)
        intentos += 1
        respuesta = input(f"¿Es tu número {intento}? (s/n) ")

        if respuesta == "s":
            print(f"¡Genial! Adivine tu número en {intentos} intentos.")
            break
        elif respuesta == "n":
            pista = input("¿Es tu número mayor (m) o menor (n) que mi intento? ")
            if pista == "m":
                rango_inferior = intento + 1
            else:
                rango_superior = intento - 1


jugar_de_nuevo = "s"
while jugar_de_nuevo== "s":
    modo = input("Elige el modo de juego (1 - Usuario adivina, 2 - Computadora adivina): ")

    if modo == "1":
        adivina_numero_usuario()
    elif modo == "2":
        adivina_numero_computadora()
    else:
        print("Modo de juego no válido.")

    jugar_de_nuevo = input("¿Deseas jugar de nuevo? (s/n) ")