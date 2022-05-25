# hacer un programa que pida 3 numeros y determine cual es el mayor
# mi respuesta (esta mal)
'''
num1 = int(input("escribe un numero-> "))
num2 = int(input("escribe un numero-> "))
num3 = int(input("escribe un numero-> "))

if num1>num2>num3:
    print("El primer numero es el mayor")
elif num1<num2>num3:
    print("El segundo numero es el mayor")
elif num1>num2<num3:
    print("El tercer numero es el mayor")
else:
    
    print("Fin del programa")'''
# respuesta correcta
num1 = int(input("escribe un numero-> "))
num2 = int(input("escribe un numero-> "))
num3 = int(input("escribe un numero-> "))

if num1>=num2 and num1>=num3:
    print(f"el numero mayor es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"el numero mayor es {num2}")    
elif num3>=num1 and num3>=num2:
    print(f"el numero mayor es {num3}")   
#else:
 #   print("son los 3 numeros iguales")
