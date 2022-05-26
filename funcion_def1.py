# funciones
'''
Es la modularizacion del codigo para llamar a la funcion las veces que se quiera
y no repetir codigo
# scopes: es como una burbuja de codigo, todo lo que hay dentro tiene sentido, 
pero desde fuera no lo tiene

-Variables globales: a lo largo de todo el codigo
-Variables locales: dentro del scope
'''
'''
reglas generales de las funciones
1.- no se ejecuta si no la llamas
2.- la puedo llamar todas las veces que quiera
3.- hay que definirlas antes de llamarla
4.- 
'''
#Funciones sin parametros
'''
def miFuncion():
    conjunto de instrucciones
'''
def derechosHumanos():
    print("Derecho a la vida")
    print("Derecho a la igualdad")
    print("Derecho a la libertad")
    # si ejecutamos aqui no va a pasar nada porque no la estamos llamando
derechosHumanos() #asi se llama a la funcion

def derechosMayorEdad():
    print("Derecho a votar")
    print("Derecho al trabajo")

# FUNCIONES CON PARAMETROS

'''
def miFuncion2(variable1, variable2):
    conjunto de instrucciones
'''
# creamos una funcion que diga segun la edad que derechos tiene la persona
def mayoriaEdad(nombre, edad):
    print(f"Segun la edad de {nombre} sus derechos son: ")
    if edad >= 18:
        derechosHumanos()
        derechosMayorEdad()
    else:
        derechosHumanos()
        
mayoriaEdad("pepito", 19)
mayoriaEdad("Jose Maria", 29)
mayoriaEdad("Dana", 17)
#tambien se puede invertir la forma de introducir los datos de la siguiente manera
mayoriaEdad(edad=19, nombre="margarita") #poniendo la variable y un = seguido edad= nombre=

# FUNCIONES CON PARAMETROS POR DEFECTO
'''
def miFuncion3(variable1, variable2=valordefecto):
    conjunto de instrucciones
'''
def mayoriaDeEdad2(edad, nombre="Una persona cualquiera"):
    print(f"Segun la edad de {nombre} sus derechos son: ")
    if edad >= 18:
        derechosHumanos()
        derechosMayorEdad()
    else:
        derechosHumanos()
mayoriaDeEdad2(10)
mayoriaDeEdad2(99)
mayoriaDeEdad2(19, "Dana")