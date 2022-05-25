'''
Realizar un juego para adivinar un numero. para ello generar un numero aleatorio
entre el 0-100, y luego ir pidiendo numeros indicando "es mayor" o "e menor"
segun sea mayor o menor con respecto a N
el proceso termina, cuando el usuario acierta, mostrar el numero de intentos
'''
import random

print("\t=====================") # \t es para poner una tabulacion entre  la t y lo que queramos
print("\t.:Adivina el número:.")
print("\t=====================")

aleatorio = random.randint(0,100) #generamos un numero aleatorio

contador = 0

while True:
    numero = int(input("Introduzca un número->"))
    contador +=1
    if numero>aleatorio:
        print("\tEl numero introducido es mayor")
    elif numero<aleatorio:
        print("\tEl numero introducido es menor")
    else:
        numero==aleatorio
        print("\n\tEse es el numero correcto")
        break
print(f"El numero de intentos a sido->{contador} ")