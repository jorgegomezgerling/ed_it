# # def sumar(x):
# #     return x + 100

# # def cuadrado(x):
# #     return x**2

def superior(funcion, lista):
    resultado = []
    for n in lista:
        resultado.append(funcion(n))
    return resultado

numeros = [9, 14, 6, 8]

print(superior(lambda x:x**2, numeros))
print(superior(lambda x:x+100, numeros))

# print(lista_estudiantes[0])
# print(lista_estudiantes[1])
# print(lista_estudiantes[1])
# print(lista_estudiantes[1])




# def ordenar(n):
#     return n.sort()

# def superior(funcion, lista):
#     ordenados = []
#     ordenar(lista)
#     return lista


# lista_estudiantes = [('pepe', 4.0),
#                      ('maria', 3.5),
#                      ('carlos', 2.8),
#                      ('juan', 1.0)]

# def retornar_nota(estudiante):
#     return estudiante[1]

# lista_ordenada = sorted(lista_estudiantes, key=lambda x:x[1])
# print(lista_ordenada)

