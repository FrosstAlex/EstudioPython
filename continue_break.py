# instrucciones continue & break se pueden utilizar en los bucles
# explicacion en for tipo range

for i in range(10):
    if i == 5:
        continue
    print(i)
'''
0
1
2
3
4
6
7
8
9
cuando llega al 5 lo ignora y sigue el programa, porque le hemos dicho que pase del 5, 
es decir que continua el bucle for sin ese parametro
'''
# Break
for i in range(10):
    if i == 5:
        break
    print(i)
print("programa finalizado")
'''
0
1
2
3
4
programa finalizado
para el programa cuando llega al 5 es decir:
cuando llega a la instruccion que le hemos dado como su palabra dice hace un break y para el bucle for

EL CONTINUE IGNORA Y SIGUE Y EL BREAK PARA EL PROGRAMA
'''