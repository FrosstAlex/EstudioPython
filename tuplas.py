'''tuplas sintaxis, son como listas pero inmutables
tuplas = ()
print(tuplas)'''

tupla = (4,"alex", 5, 7, 9,4)
print(tupla)
'''
con las tuplas, no se puede añadir, ni borrar. lo unico que se puede hacer es buscar elementos añadidos al crearlas
'''
#print(4 in tupla) # salida terminal True
'''los comandos de busqueda serian
in, ejemplo print(4 in tupla)
.count print(tupla.count(4)) retorna 2 que es el valor de las veces que esta repetida la busqueda
.index ejemplo print(tupla.index(4)) daria como resultado 4 que es el indice 0
print(len(tupla)) para saber cuantos elementos tiene
'''

#libro = ("grande", "pequeño", 2, 4, 6, 8)
#libro.append("rojo")
'''
libro.append("rojo")
AttributeError: 'tuple' object has no attribute 'append'
NO SE PUEDE AÑADIR PORQUE ES UNA TUPLA
'''
'''
se pueden transformar tuplas en listas, y listas en tuplas ejemplo
'''
libro = ("grande", "pequeño", 2, 4, 6, 8)
libreria = list(libro)
print(type(libreria)) # <class 'list'> aqui tenemos el cambio ya realizado, y podemos modificar la lista

# y viceversa, se pueden transformar listas en tuplas
mesa = ["grande", "pequeña", "redonda", 1, 2, 3]
mesas = tuple(mesa) # primero el nombre de la futura tupla = tuple(nombre de la lista)  SINTAXIS
print(type(mesas)) # salida terminal <class 'tuple'>
# las tuplas son mas rapidas de ejecucion y pesan menos en memoria 