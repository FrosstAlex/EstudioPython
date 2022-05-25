'''
ejercicio 2
Escribir un programa  que tenga dos listas y que a continuacion cree las siguientes 
listas(en las que no debe haber repeticiones)
1.- Lista de elementos que aparecen en las dos listas
2.- Lista de elementos que aparecen en la primera lista, pero no en la segunda
3.- Lista de elementos que aparecen en la segunda lista, pero no en la primera
4.- Lista de elementos que aparecen en ambas listas
'''
'''
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [7,8,9,10,11,12,14]
print (list1)
print (list2)
print (list1[0:6])
print (list2[3:])
print (list1[0:6],(list2[3:]))'''
# SOLUCION
lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]
# Eliminar elementos repetidos en ambas listas
a = set(lista1)
b = set(lista2)
union = list(a | b)
soloA = list(a -b)
soloB = list(b -a)
interseccion = list(a&b)
print(f"Lista de elementos que aparecen en las dos listas {union}") 
print(f"Lista de elementos que aparecen en la primera lista, pero no en la segunda{soloA}")
print(f"Lista de elementos que aparecen en la segunda lista, pero no en la primera{soloB}")
print(f"Lista de elementos que aparecen en ambas listas{interseccion}")