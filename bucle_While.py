'''
BUCLE WHILE

los bucles son un trozo de codigo que se repite 
un numero indeterminado o determinado de veces
while se le conoce como un numero indterminado de veces
se necesita que se cumpla una determinada condicion para que se 
repita n veces

EJEMPLO 1
import math
numero = int(input("Introduzca un numero-> "))
while numero<0:  # sintaxis, while luego condicion(que se pueden poner varias con operadores logicos and not or)
    print(" Error-> Deberia ser un numero positivo")
    numero = int(input("Introduzca un numero-> "))
print(f"\nLa raiz cuadrada es: {(math.sqrt(numero)):.2f}")
'''
i = 0
while i<10:
    print(i)
    i +=1 # Aumenta la condicion en +1
    