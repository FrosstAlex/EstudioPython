'''
hacer un programa que pida una cadena por teclado, 
luego meta los caracteres en una lista sin repetir caracteres
'''
'''
cadena = str(input("Escriba una frase->"))
cadena2 = cadena
cadena = set(cadena2)
cadena = {cadena2}
cadena = list(cadena)   SE PUEDE HACER CON CONJUNTOS PERO ES MAS FACIL CON UN BUCLE FOR 
                        DICIENDOLE QUE HAGA UNA LISTA DE LA CADENA Y 
                        QUE SI LA LETRA POR LA K VA ESTA DENTRO QUE LA IGNORE
print(cadena2)'''


# Solucion

cadena = input(" introduzca una cadena->")

lista = [] # lista vacia para introducir caracteres, y como va de 1 en 1 ignora los que ya estan dentro

for i in cadena: #recorremos la cadena
    if i not in lista: # si el caracter por ql k vamos no esta en la lista
        lista.append(i) #lo agregamos a la lista

print(f"\nLista de carcteres sin repetir \n{lista}")

