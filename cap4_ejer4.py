# hacer un programa para sumar numeros pares dentro de un rango
# ejemplo: suma de numeros pares del 2 al 30 suma = 240

'''numeros = list(range(2, 31, 2))# me hace una lista [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
print(numeros)
suma =
'''
# Solucion

a = int(input("introduzca el inicio a sumar->"))
b = int(input("introduzca el final a sumar->"))
suma = 0
for i in range(a,b+1):
    if i%2==0: #si el numero es par
        suma += i
print(f"\nLa suma es: {suma} ")
'''
introduzca el inicio a sumar->1
introduzca el final a sumar->30

La suma es: 240
'''