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

def fibonacci(numero):
    if ((numero == 0) or (numero == 1)):
        return numero
    else:
        return fibonacci(numero) + fibonacci(numero - 1)

print(fibonacci(2))