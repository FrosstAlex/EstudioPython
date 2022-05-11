'''
hacer un programa para cambiar el valor
de dos variables
ejemplo
a = 10  a = 5
b = 5   b = 10

a = 10
b = 5
resultado1 = a -5  
resultado2 = b + 5
print(f"El resultado es:\n {resultado1}\n{resultado2}")
'''
# Respuesta correcta

a = input("a ->")
b = input("b ->")

a,b = b,a #Intercambia al valor de las variables
print(f"el nuevo valor de a es: {a}")
print(f"el nuevo valor de b es: {b}")
