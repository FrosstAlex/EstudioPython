'''
hacer un ejercicio donde se debera imprimir por consola la palabra con mas caracteres de dos palabras dadas
en el caso de que ambas tengan la misma cantidad de caracteres deberias mostrar el mensaje
son iguales
'''

#solucion
cadena1 = input("introduzca una palabra-> ")
cadena2 = input("introduzca una palabra-> ")
if len(cadena1) > len(cadena2):
    print(f"\nLa cadena mas larga es {cadena1} ")
elif len(cadena1) < len(cadena2):
    print(f"\nLa cadena mas larga es la {cadena2} ")
    
else:
    len(cadena1)==len(cadena2)
    print("Ambas cadenas son iguales")
    
    
#(===================================================================================================)

#EJERCICIO 2
'''
hacer un ejercicio para determinar si una frase introducida por el usuario finaliza 
con un punto o no. Deberias imprimir por consola una de las siguientes opciones
termina con punto 
no termina con punto
'''

#solucion mia
frase = input("Introduzca una frase-> ")

if frase.endswith("."):
    print("Termina con punto")
else:
    print("No termina con punto")