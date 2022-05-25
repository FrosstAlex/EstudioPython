'''Ejercicio 1
Hacer un programa que cambie el valor de 2 variables ejemplo:
a=10  a=5
b=5   b=10
a = input("introduzca lo que quiera->")
b = input("introduzca lo que quiera->")
# a,b = b,a
a,b = b,a
print(a,b)
'''
'''
ejercicio2
Hacer un programa que calcule el % de descuento ejemplo:
En una tienda ofrecen el 15% de descuento y el cliente desea saber cuanto va a pagar
'''
precio = float(input("Introduzca el precio del producto->"))
descuento = float(input("Introduzca el porcentaje de descuento->"))
precio_descuento = precio * descuento/100
#total = precio - precio_descuento 
mas_menos = (input("Introduzca - para descontar + para aumentar el por ciento->"))
if mas_menos == ("-"):
    total = precio - precio_descuento
elif mas_menos == ("+"): 
    total = precio + precio_descuento
print(f"\nEl precio total es de {total}€ ")

'''
else:
    print("Introduzca + ó - solamente")   NO FUNCIONA EL ELSE
    Traceback (most recent call last):
  File "/home/alex/Documentos/estudios/programacion/estudio/repeticion_ejercicios/ejercicio1.py", line 20, in <module>
    mas_menos = float(input("Introduzca - para descontar + para aumentar el por ciento->"))
ValueError: could not convert string to float: 'p
'''         

