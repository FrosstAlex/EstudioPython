# pide numeros y metelos en una lista cuando el usuario meta un 0
# ya dejaremos de insertar. por ultimo, muestra los numeros ordenados de menos a mayor
'''
numero = []
numero = int(input(" introduce numeros, para parar introduzca 0->"))
while numero==0:
    break
print(numero.sort)
SALIDA TERMINAL
 introduce numeros, para parar introduzca 0->10
Traceback (most recent call last):
  File "/home/alex/Documentos/estudios/programacion/estudio/cap4_ejer3.py", line 8, in <module>
    print(numero.sort)
AttributeError: 'int' object has no attribute 'sort'
'''

#Solucion

lista = []
salir = False
while not salir:
    numero = int(input("Inserte los numeros->"))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()
print(f"lista ordenada: \n{lista}")