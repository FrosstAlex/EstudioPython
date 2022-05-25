# Condicionales
'''
los condicionales en Python son 3 if, elif, else y se usan de la siguiente manera
if la condicion:
    print(la condicion)
elif la condicion: #se pueden poner los elif que se quieran, no hay limite
    print(la condicion de elif)
else:        #else se utiliza siempre el ultimo y es el que dice, si las condiciones de arriba no se cumplen, yo te lo digo
    print(la condicion de else)
EJEMPLOS este programa te dice si es positivo o negativo el numero
'''
numero = int(input("Introduzca un numero-> "))
if numero>0:       
        #Primero la condicion if luego la variable numero y luego la instruccion >0(menor que 0) y al final los dos puntos:
        #el print de abajo responde a si se cumple la condicion
    print("El numero es positivo")
    '''aqui podriamos seguir con el codigo,  siempre que respetemos la identacion
    if la condicion
    elif la condicion
    else:
        la accion    '''
elif numero==0: #elif es igual que if se pone la condicion elif la instruccion y los :(dos puntos finales)
    print("El numero es 0 ni positivo ni negativo")
else:    # el condicional else siempre se pone asi else: y en la linea de abajo el codigo
    print("El numero es negativo")
        
print("fin del programa")  #este print esta relacionado con la primera condicion if
    
