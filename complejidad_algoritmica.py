def testtime(fun):
    from time import time

    def wrap(*args, **kwargs):
        inicio = time()
        resultado = fun(*args, **kwargs)
        final = time()
        print(f"la funcion {fun.__name__} tardó {final-inicio}")
        return resultado
    
    return wrap

@testtime
def suma(m,n):
    resultado = 0
    for num in range(m, n+1):
        resultado += num
    return resultado

@testtime
def suma_constante(m:int, n:int) -> int :
    if (dif := abs(m-n)) % 2 == 0:
        suma = (dif//2) * (m+n) + ((m+n)//2)
    else:
        suma = ((dif//2)+1) * (m+n)
    return suma

suma_constante(0,1000000000)
suma(0,1000000000)
