'''
Bucles for
son bucles que se repiten un numero determinado de veces
se utiliza con colecciones
'''
'''for casa in ["comedor", "sofa", "silla", "cocina"]:
    print(casa) ejemplo mio '''
'''    
for i in [10,5,7,9,3,"Alejandro"]: # la i es una variable
    print("hola mundo") # te imprime hola mundo tantas veces como elementos hay en la coleccion
    
for i in [10,5,7,"Maria",3,"Alejandro"]: 
    print(f"Elemento: {i}") 
 SALIDA TERMINAL
Elemento: 10
Elemento: 5
Elemento: 7
Elemento: Maria
Elemento: 3
Elemento: Alejandro

Tambien se puede utilizar con diccionarios, tuplas, listas, conjuntos
'''
coleccion = {"Alejandro":39, "Maria":33, "jose":45, "Jose Maria":29}
for i in coleccion:
     print(f"Elemento:{i}") #Imprime  las claves del diccionario
'''
SALIDA TERMINAL
Elemento:Alejandro
Elemento:Maria
Elemento:jose
Elemento:Jose Maria
'''

coleccion = {"Alejandro":39, "Maria":33, "jose":45, "Jose Maria":29}
for i in coleccion:
     print(f"{coleccion[i]}") #Imprime el valor del diccionario     
'''
39
33
45
29   
'''
#coleccion = {"Alejandro":39, "Maria":33, "jose":45, "Jose Maria":29}
#for i in coleccion:
#     print(f"{i} -> {coleccion[i]}") #Imprime la clave y el valor del diccionario
'''
Alejandro -> 39
Maria -> 33
jose -> 45
Jose Maria -> 29
'''
coleccion = {"Alejandro":39, "Maria":33, "jose":45, "Jose Maria":29}

for clave,valor in coleccion.items(): #recorre elementos dentro de un diccionario
     print(f"{clave} {valor}") # esta es la forma correcta 
'''
Alejandro 39
Maria 33
jose 45
Jose Maria 29
'''
coleccion = "Alejandro"
for i in coleccion:
     print(f"{i}")
'''
A
l
e
j
a
n
d
r
o
'''

coleccion = "Alejandro"
for i in coleccion:
     print(f"{i}", end= " ")
# A l e j a n d r o 

coleccion = "Alejandro"
for i in coleccion:
     print(f"{i}", end= "/")
# A/l/e/j/a/n/d/r/o/