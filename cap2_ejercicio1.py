# Ejercicio 1 capitulo 2  hacer un programa que pida dos numeros 
# y te diga cual es par y cual impar o si ambos lo son

#num1 = int(input("Introduzca un numero-> "))
#num2 = int(input("Introduzca otro numero-> "))

'''mi respuesta
if num1%2==0 and num2%2==0:
    print("Los dos numeros son pares")
elif num1%2==0:
    print("El primer numero es par")
elif num2%2==0:
    print("El segundo numero es par")
else:
    print("ninguno de los dos es par")
'''
# La respuesta correcta
num1 = int(input("Introduzca un numero-> "))
num2 = int(input("Introduzca otro numero-> "))

if num1%2==0 and num2%2==0:
    print("Ambos numeros son par")
elif num1%2==0 and num2%2!=0:
    print(f"El primer numero es par")
elif num1%2!=0 and num2%2==0:
    print(f"El segundo numero es par")
else:
    print("Ninguno de los dos es par")