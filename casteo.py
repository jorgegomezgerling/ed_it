# a = 9
# print(type(a))

# print(a + 1)

# b = str(a)

# print(type(str(b)))

# print(b + "1")

# print(id(a), id(b))

# c=id(1)
# d=id(2)

# print(c, d)

# print(dato:='hola')

# print(f"mi nombre es:", dato:=input('nombre: '))

# for i in range(1, 10):
#     list(i)

# def sumar(*args):
#     return sum(args)

# print(sumar(1,2,3))
numeros = []
def fibonacci(numero):
    if ((numero == 0) or (numero == 1)):
        return numero
    else:
        numero = fibonacci(numero - 1) + fibonacci(numero - 2)
        return numero


print(fibonacci(9))

# Utilizando un bucle “while”, elaborar un código
# que imprima en pantalla cada uno de los
# elementos de una lista y simultáneamente los
# elimine, hasta quedar vacía.


# numeros = [1, 2, 3]

# while numeros:
#     print(numeros.pop())

# print(numeros)