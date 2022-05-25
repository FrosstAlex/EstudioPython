# hacer un programa que pida un numero por teclado y guarde en una lista su tabla de multiplicar hasta el 10

numero = int(input("Introduzca un numero-> "))
lista = []
for i in range(1,11):
    lista.append(i*numero) # iterador i multiplicado por el numero que introduce input
print(f"\nLa tabla de multiplicar es:\n{lista}")