'''bucle for tipo range
si queremos que el bucle haga un numero de repeticiones concreta, 
sin crear una coleccion con los elemento
'''
#for i in range(10): # range crea una coleccion ficticia con 10 elementos o los que sea
#    print("Hola Mundo") 
'''Imprimira 10 veces hola mundo
Hola Mundo
Hola Mundo
Hola Mundo
Hola Mundo
Hola Mundo
Hola Mundo
Hola Mundo
Hola Mundo
Hola Mundo
Hola Mundo'''

#for i in range(5, 11): # Tambien se puede poner de un rango a otro 
#    print(i)
'''
5
6
7
8
9
10
'''

for i in range(2, 21,2): 
    print(i)
'''
otro ejemplo, quiero mostrar los pares del 0 al 20(siempre llega hasta -1 en el rango que pongamos)
poniendo ,2 lo que hara sera ir de 2 en 2 hasta el rango que este puesto
IGUAL A LA INVERSA
for i in range(21,2,-2) se pone -2 porque queremos que descuente de 2 en 2
SALIDA TERMINAL
2
4
6
8
10
12
14
16
18
20
'''
