# Cree una función llamada “superior”, que reciba por
# argumento una función y una lista. La función que se
# pasa por argumento a superior debe elevar al cubo un
# # número y retornarlo. Para que luego al aplicarla en la
# # de orden superior, esa operación se realice miembro
# # a miembro de la lista.
# # Para finalizar la función “superior” debe de devolver
# # una nueva lista.

# # numeros = [3, 4, 5]

# # def superior(funcion, lista):
# #     new_lista = []
# #     for i in lista:
# #         new_lista.append(funcion(i))
# #     return new_lista

# # print(superior(lambda x:x**3, numeros))


# # Crear un programa que solicite dos números
# # en consola e imprima el resultado de las
# # cuatro operaciones aritméticas aplicadas
# # sobre ellos. Por ejemplo (en rojo la entrada
# # del usuario):


# def calculadora(n1, n2):
#     print(n1 + n2)
#     print(n1 - n2)
#     print(n1 * n2)
#     try:
#         print(n1 / n2)
#     except ZeroDivisionError:
#         print("No se puede dividir por cero")

# try: 
#     numero1 = int(input("Escribe un número: "))
#     numero2 = int(input("Escribe otro número: "))
#     calculadora(numero1, numero2)
# except ValueError:
#     numero1 = int(input("Escribe un número: "))
#     numero2 = int(input("Escribe otro número: "))
#     calculadora(numero1, numero2)
# except ZeroDivisionError:
#     print("No se puede dividir por cero")



# def obtener_numero(mensaje):
#     while True:
#         try:
#             return float(input(mensaje))
#         except ValueError:
#             print("Debes ingresar un número válido. Intenta de nuevo.")

# def calculadora(n1, n2):
#     print(n1 + n2)
#     print(n1 - n2)
#     print(n1 * n2)
#     try:
#         print(n1 / n2)
#     except ZeroDivisionError:
#         print("No se puede dividir por cero")

# n1 = obtener_numero('Ingrese primer número: ')
# n2 = obtener_numero('Ingrese segundo número: ')
# calculadora(n1, n2)


# numero1 = obtener_numero("Escribe un número: ")
# numero2 = obtener_numero("Escribe otro número: ")
# calculadora(numero1, numero2)

# Codigo interesante, re-implementar. 

# texto = 'python'
# texto2 = []

# for letra in texto:
#     if (letra == 'p' or letra == 't'):
#         texto2.append(letra.upper())
#     else:
#         texto2.append(letra)

# print(''.join(texto2))

# mas_facil = texto.capitalize()
# print(texto.capitalize())
# print(mas_facil)

# cancion = "Si un amor cayó del cielo No pregunto más En mis sueños nunca pierdo La oportunidad Ah, ah, ah, ah Aunque a veces se equivoquen No confundo más Voy a hacer que mis cenizas Vuelvan al papel Ah, ah, ah, ah Ah, ah, ah, ah Siempre es hoy Ya es parte de mi ser Siempre es hoy Lo claro entre los dos Siempre es hoy Sos parte de mi ser Quiero hacer Cosas imposibles Cosas imposibles Ah Ah, ah, ah, ah Mutacion del porvenir Es eternidad No me hablen de esperanzas vagas Persigo realidad Ah, ah, ah, ah Ah, ah, ah, ah Siempre es hoy Ya es parte de mi ser Siempre es hoy Lo claro entre los dos Siempre es hoy Sos parte de mi ser Quiero hacer Cosas imposibles Cosas imposibles Quiero hacer Cosas imposibles Cosas imposibles"

# print(cancion.count("Cosas imposibles"))

# texto_original = """Quiero hacer
# Cosas imposibles
# Cosas imposibles

# Quiero hacer
# Cosas imposibles
# Cosas imposibles


# Agregar a favoritos

# Agregar a playlist

# Tamaño de la fuente"""

# print(texto_original.find("Agregar"))