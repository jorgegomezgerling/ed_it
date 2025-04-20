# Cree un algoritmo para guarda cada una de las
# personas del diccionario personas en un txt.
# El nombre se tiene que guardar en minúsculas y
# cada persona debe quedar en un renglón con un
# guión del medio separando el nombre y la edad.
# Ejemplo dentro del personas.txt se tendría que ver:
# roberto-20
# romina-32

personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19, "Marquitos Navaja": 10}

# with open("archivo2.txt", "w") as f:

#     for persona in personas:
#         f.write(persona.lower())
#         f.write("-")
#         f.write(str(personas[persona]) + '\n')

# Cree un algoritmo para volver al diccionario original
# desde el archivo personas.txt creado en el ejercicio
# anterior.
# El nombre se tiene que recuperar en mayúsculas y
# cada valor debe volver a ser del tipo entero.
# El diccionario tendría que volver a verse como:
# personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

with open("archivo2.txt", "r") as f:
    dict = {}

    for linea in f.readlines():
        
        linea = linea.split("-")
        dict[linea[0].capitalize()] = int(linea[1].replace("\n", ""))
    
    personas = dict
    print(personas)
    
    
    





# f.write("hola")