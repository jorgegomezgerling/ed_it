# >>> nombre = "Pablo"
# >>> edad = 30
# >>> mensaje = "Hola, mi nombre es {0}. Tengo {1} años."
# >>> mensaje.format(nombre, edad)

# nombre = 'juan'
# edad = 30
# mensaje = 'hola, mi nombre es {0}. tengo {1} years old.'

# print(mensaje.format(nombre, edad))

# Ejercicio 1: Mayúsculas
# Se tiene una lista de personas como la siguiente:
# Se desea crear una función que ponga mayúscula
# solo en la primera letra, tanto del nombre como del
# apellido, y que devuelva la lista con esta
# modificación.
# Se puede usar funciones de orden superior para
# resolver el ejercicio, no hay limitaciones.

nombres = ["juan salvo","henry courtney","elizabeth bennet","marge simpson"]

def mayusculas(funcion, lista):
    new_list = []
    for i in lista:
        new_list.append(funcion(i))
    return new_list

print(mayusculas(lambda x:x.title(), nombres))