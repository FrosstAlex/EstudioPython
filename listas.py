# listas
'''
sintaxis:
lista = []
print(lista)'''

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
print(dias)

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
print(dias[4]) 
'''para imprimir algo dentro de una lista elegir el indice sabiendo que empieza por 0
imprimir a la inversa utilizar indices negativos -1(es viernes)
'''
dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
print(dias[0:4]) #para imprimir de un punto a otro, imprimira hasta el indice anterior al indicado

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", 1, 0.67, ["otralista"], True]
print(dias) 

'''
SALIDA TERMINAL
['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
viernes
['lunes', 'martes', 'miercoles', 'jueves']
['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 1, 0.67, ['otralista'], True]
'''

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", 1, 0.67, ["otralista"], True]
print(len(dias)) # te indica el numero de elementos de la lista 
#(las listas dentro de las listas te las indica como 1 elemento)

'''
para añadir elementos a la lista se usa el parametro append el cual lo añade al final de la lista
para añadir un elemento organizado se usa .insert
ejemplo
'''
dias = ["lunes", "martes", "miercoles", "viernes", 1, 0.67, ["otralista"], True]
dias.append("jueves")
print(dias)
#Terminal ['lunes', 'martes', 'miercoles', 'viernes', 1, 0.67, ['otralista'], True, 'jueves'] se a añadido jueves al final

dias = ["lunes", "martes", "miercoles", "viernes", 1, 0.67, ["otralista"], True]
dias.insert(3, ("jueves")) #seleccionando el indice lo agrega
print(dias)
#Terminal ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 1, 0.67, ['otralista'], True] añadido en su sitio

'''
para añadir mas de un elemento se usa el parametro .extend
ejemplo
'''

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", ]
dias.extend(["sabado", "domingo"]) #se añaden al final de la lista
print(dias)
# Terminal ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", ]
print("miercoles" in dias) # esto es una forma de saber(buscar) si hay un elemento dentro de una lista
#terminal  True te lo devuelve como un booleano

#dias = ["lunes", "martes", "miercoles", "jueves", "viernes", ]
#print(dias.index("sabado"))
'''
salida terminal
Traceback (most recent call last):
  File "/home/alex/Documentos/estudios/programacion/estudio/listas.py", line 63, in <module>
    print(dias.index("sabado"))
ValueError: 'sabado' is not in list
ESTE ERROR ES PORQUE SABADO NO ESTA EN LA LISTA
'''

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", ]
print(dias.index("lunes")) # terminal 0 porque 0 es el indice donde esta "lunes"

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "lunes", "miercoles"]
print (dias.count("lunes")) #este parametro te cuenta cuantos valores "lunes" hay dentro de la lista 2

# como eliminar parametros de una lista

dias = ["lunes", "martes", "miercoles", "jueves", "viernes",]
dias.pop() #solo puesto asi te elimina el ultimo elemento de la lista en este caso viernes
dias.pop(0) #elimina el lunes
dias.remove("miercoles") # elimina por elemento en este caso miercoles
# dias.clear #esto te elimina todos los elementos de una lista
dias.reverse #le da la vuelta a la lista
 #  dias = ["lunes", "martes", "miercoles", "jueves", "viernes",]*2 se copian todos los elementos 2 veces 
 # se pueden copiar todas las veces que se quieran
dias = [7,9,5,8,1,3,-7]
dias.sort() #te ordena la lista salida terminal [-7, 1, 3, 5, 7, 8, 9] los ordena ascendente
dias.sort(reverse=True) #te ordena la lista salida terminal [9, 8, 7, 5, 3, 1, -7] los ordena descendente
print(dias)
'''
Salida terminal
['martes', 'jueves']
dias.pop()
dias.pop(0)
dias.remove("miercoles)
con lo eliminado nos quedariamos solo con 2 elementos en la lista, martes y jueves
'''