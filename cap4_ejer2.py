# Llenar una lista con los numeros del 1 al 10
# luego modificar los elementos de la lista multiplicandolos 
# por el valor que el usuario digite
'''
listNum = list(range(1, 10)) y encima he llegado al numero 9 no al 10 recuerda que siempre es -1 
mult_num = int(input("Introduzca el numero por el que desea multiplicar la lista->")) * listNum
print(listNum)
mi error es que lo estoy multiplicando por la lista, no por el contenido de ella
'''
# Solucion
'''
list_num = list(range(1,11))
print("Lista original: ")
for i in list_num:
    print(i, end="-")
valor = int(input("\nDigite un valor para multiplicar-> "))

# multiplicar los elementos de la list_num
indice = 0
for i in list_num:
    list_num[indice] *= valor
    indice += 1
print(f"\nLista final con los elementos multiplicados por",(valor))
print(list_num)

SALIDA TERMINAL
Lista original: 
1-2-3-4-5-6-7-8-9-10-
Digite un valor para multiplicar->2

Lista final con los elementos multiplicados por 2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
# Otra forma de hacerlo

list_num = list(range(1,11))
print("Lista original: ")
for i in list_num:
    print(i, end="-")
valor = int(input("\nDigite un valor para multiplicar-> "))
print("Lista original: ")
# multiplicar  los elementos
for indice, i in enumerate(list_num): # Esto crea un indice automatico(de hay indice) y luego un iterador que es la i
    list_num[indice] *= valor
print(f"\nLista final con los numeros multiplicados por {valor}")
for i in list_num:
    print(i,end=" ")
'''
Lista original: 
1-2-3-4-5-6-7-8-9-10-
Digite un valor para multiplicar-> 2
Lista original: 

Lista final con los numeros multiplicados por 2
2 4 6 8 10 12 14 16 18 20                                                                  
'''