# Crear un script que solicite al usuario el
# código de un país e imprima su nombre,
# de acuerdo con el siguiente diccionario:
# # Diccionario código: país.

paises = {
    "ar": "Argentina",
    "es": "España",
    "us": "Estados Unidos",
    "fr": "Francia"
}


# print(paises["ar"])
# print(paises["din"])



# Si el código ingresado no se encuentra en
# el diccionario, debe imprimir un mensaje en
# pantalla y volver a preguntar. Si el usuario
# escribe “salir”, el programa debe terminar.

# def obtener_pais(mensaje):
#         try:
#             return paises[mensaje]
#         except KeyError:
#             print("El código ingresado no es correcto")

# def imprimir_pais(function):
#     pais = input("Por favor, ingrese código de área: ")



while True:
    codigo = input("Ingrese un codigo: ")
    if codigo == "salir":
        break
    try:
        print(paises[codigo])
    except KeyError:
        print("El código es invalido, vuelve a intentarlo.")

# print(obtener_pais("ga"))
# print(obtener_pais("fr"))

