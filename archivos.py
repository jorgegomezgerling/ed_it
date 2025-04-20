# f = open("mi_archivo.txt", "r")

# print(f.readlines())

# lista = f.readlines()

# print(type(lista), lista)

# f.close()

# with open('mi_archivo.txt', "a") as f:

#     f.writelines(["\nEnsalada de remolacha","\nCaracamomo","\nBaladí"])


import json

with open("mi_archivo.txt", "r") as f:

    texto = f.read()

# with open("mi_archivo.txt", "r") as f:

#     texto2 = f.readlines()


lista = texto.split('\n')
# print(lista)


def contar(lista):
    dict = {}
    for item in lista:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict

diccionario_de_datos = contar(lista)

print(diccionario_de_datos)

# print(json.dumps(diccionario_de_datos))


{'saracatunga unga unga': 1, 'juan el tornero': 1, 'milanesas al espiedo': 1, 'lasaratrabaja': 1, 'Termo matutino': 1, 'Termo vespertino': 1, 'Termo nocturno': 1, 'Ensalada de remolacha': 9, 'Caracamomo': 9, 'Baladí': 9, 'Incienso': 1, 'Papel Mache': 1, 'Tragaluz': 1, 'Concepcion del Uruguay': 1, 'Toyota Corolla': 1, 'ppp': 1}


# print(lista)

# print(type(texto), type(lista))

# print(texto2)
# print(type(texto2))

