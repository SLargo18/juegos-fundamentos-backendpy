import random
import string

def generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiales):
    caracteres = ""

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasena


longitud = int(input("Ingresa la longitud de la contraseña dada en valor numerico: "))
incluir_mayusculas = input("vas a incluir mayúsculas? (s/n) ") == "s"
incluir_minusculas = input("y minúsculas? (s/n) ") == "s"
incluir_numeros = input("alungos números? (s/n) ") == "s"
incluir_caracteres_especiales = input("¿por ultimo deseas incluir caracteres especiales? (s/n) ") == "s"

contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_caracteres_especiales)
print(f"La contraseña generada es: {contrasena}")