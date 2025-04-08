# Crear un bucle que almacene en una variable la
# suma de todos los elementos numéricos de una
# lista, con excepción del último.


numeros = (1, 5, 31, 15)
suma = 0

for i in numeros[:-1:]:
    suma += i

# print(suma)

dic = {"a": 1, "b": 2, "c": {"d": "e", "y": "h"}, "f": {"h": "i"}}

# print(dic['c']['y'])


# Unpacking! 

t = (1, 2, 3)

a, b, c = t

print(b)