# Hacer un programa para calcular el factorial de un numero positivo

#Solucion
numero = int(input("Digite un numero->"))
while numero<0: #mientras el numero sea negativo
    print("El numero tiene k ser positivo")
    numero = numero = int(input("Digite un numero->"))
# calcular el factorial
factorial = 1
for i in range(1, numero+1):
    factorial *= i
print(f"\nEl factorial de numero {numero} es {factorial}:")