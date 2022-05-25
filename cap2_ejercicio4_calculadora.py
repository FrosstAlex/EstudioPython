# construir un pograma que simule el funcionamiento de una calculadora
# que puede  puede realizar las 4 operaciones basicas suma resta multiplicacion division
# el usuario debe especificar la operacion con el primer caracter

# calculadora

'''operacion = input("Introduzca la operacion (s r m d)-> ").lower()
num1 = float(input("Introduzca un numero-> "))
num2 = float(input("Introduzca un numero-> "))

if operacion == 's':
    print(num1 + num2)
elif operacion == 'r':
    print(num1 - num2)
elif operacion == 'm':
    print(num1 * num2)    
elif operacion == 'd':
    print(num1 / num2)
    '''
    
# Solucion

num1 = float(input("Introduzca un numero-> "))
num2 = float(input("Introduzca un numero-> "))
print(" Para suma usa- S, para resta usa -R, para multiplicacion usa M, para division usa D")
operacion = input("Introduzca la operacion-> ").upper()

if operacion=='S':
    suma = num1 + num2
    print(f"\nLa suma es: {suma}")

elif operacion=='D':
    division = num1 / num2
    print(f"\nLa division es: {division:.2f}")
    
elif operacion=='M':
    multiplicacion = num1 * num2
    print(f"\nLa multiplicación es: {multiplicacion}")
    
elif operacion=='R':
    resta = num1 - num2
    print(f"\nLa resta es: {resta}")
else:
    print("\nOperacion invalida")
    