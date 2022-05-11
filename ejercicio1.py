# Ejercicio 1:
''' escribe la siguiente expresion en forma algoritmica 
a elevado a 3 x b elevado a 2 - 2ac /2b
'''
#resultado
#a = 10
#b = 20
#c = 30
#a**3 * (b**2 - 2ac)/2b

#respuesta correcta
a = float(input("a ->"))
b = float(input("b ->"))
c = float(input("c ->"))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)

print(f"el resultado es {resultado}")
