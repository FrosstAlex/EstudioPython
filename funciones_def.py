# funciones
'''
Reglas generales de las funciones
1.- para ejecutar una funcion tienes que llamarla
2.- se puede llamar las veces que se quiera
3.- primero hay que definir la funcion, y despues llamarla
'''

#Funciones sin parametros
'''
def miFuncion(): #dentro de los parentesis pondremos los parametros de la funcion
'''
def derechos_humanos():
    print("Derecho a la vida")
    print("Derecho a la igualdad ante la ley")
    print("Derecho a la libertad")
derechos_humanos() #asi se llama a la funcion

def derechos_mayorEdad():
    print("Derecho a votar")
    print("Derecho a trabajar")

#funciones con parametros
'''
def miFuncion2(variable1, variable2):
    #conjunto de instrucciones
'''
def mayoria_edad(nombre, edad):
    print(f"Segun la edad de {nombre}, sus derechos son: ")
    if edad >= 18:
        derechos_humanos()
        derechos_mayorEdad()
    else:
        derechos_humanos()
mayoria_edad("Alex", 39)
mayoria_edad("Mari", 24)
mayoria_edad("josemaria",9)

    