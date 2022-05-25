# condicionales combinados   ejemplo con programa que identifica la edad introducida

'''
Importante la estructura!!!
'''
'''edad = int(input("Ponga su edad-> "))

if edad>=18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

condicionales anidados, es un condicional dentro de otro 
ejemplo
'''
'''edad = int(input("Ponga su edad-> "))

if edad>0: # esto es, si la edad es mayor a cero
    print("Edad correcta")
    if edad>=18:
        print("Eres mayor de edad")
else:
    print("Edad incorrecta")'''
                                     # ahora un ejemplo con  and que es el que mas pega pero tb se puede usar or not
                                     
edad = int(input("Ponga su edad-> "))

if edad>0 and edad<100:                              # esto es, si la edad es mayor a cero
    print("Edad correcta")
    if edad>=18:
        print("Eres mayor de edad")
else:
    print("Edad incorrecta")
    
edad = int(input("Ponga su edad-> "))

if edad>0 or edad<100:      # aqui una de las 2 condiciones tiene que cumplirse para continuar el programa
    print("Edad correcta")
    if edad>=18:
        print("Eres mayor de edad")
else:
    print("Edad incorrecta")
    
edad = int(input("Ponga su edad-> "))

if not(edad>0 and edad<100): # esto es la forma de poner el not y significa, si no es verdad que eres mayor k 0 y menor que 100
    print("Edad correcta")
    if edad>=18:
        print("Eres mayor de edad")
else:
    print("Edad incorrecta")

#otra forma mas abreviada de ponerlo
edad = int(input("Ponga su edad-> "))
    
if 0<edad<100:       # esto es, una forma abreviada de poner esto edad>0 and edad<100:  
    print("Edad correcta")
    if edad>=18:
        print("Eres mayor de edad")
else:
    print("Edad incorrecta")
