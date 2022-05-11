#funciones integradas
'''
sirve para hacer conversiones entre tipos de datos
ejemplo
a = ("10") esto es cadena de caracteres
a = int("10) esto es un numero entero, por asignarlo con int 
igual pasa con float
'''
#conversion de valor numerico a cadena
n = str(10) #ese 10 es cadena de caracteres, igual pasa si usamos un float
print(n)
#pasar de un valor entero a binario
n = bin(10) #esto lo pasa a binario bin
print(n)
n = hex(10) #esto lo pasa a hexadecimal
print(n)
n = int("0b1010", 2) # 2 es la base de binario
print(n)
n = int("0xa", 16) # 16 es la base de hexadecimal
print(n)


n = abs(-8) #te muestra el valor absoluto hacia el 0
print(n)

n = round(5.6) #te redondea un numero hacia el entero mas cerca en este caso seria el 6
print(n)

n = len("hola alejandro lorente muñoz") #te muestra el numero de caracteres en la cadena
print(n)


'''
Salida consola

10
0b1010
0xa
10
10
8
6
28
'''
