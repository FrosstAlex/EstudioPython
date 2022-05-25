# Ejercicio 1 Llena una lista con ls numeros del 1 al 50, luego mostrarla con un bucle for, 
# los elementos deben mostrarse de la siguiente forma 1-2-3-4-5-6-50

'''for i in range(1,51):
    print(i, end="-")

SALIDA TERMINAL
1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-
26-27-28-29-30-31-32-33-34-35-36-37-38-39-40-41-42-43-44-45-46-47-48-49-50-
'''
'''
# Solucion
lista = []
# agregamos a la lista los elementos del 1 al 50
i = 1
while i<=50:
    lista.append(i)
    i+=1
# imprimiendo los elementos de la lista
for i in lista:
    print(i, end="-")
'''
#otra forma
    
lista = list(range(1,51))
for i in lista:
    print(i, end="-")
