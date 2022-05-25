# Hacer un programa que pida un caracter e indique si es una voca o no

'''caracter = input("Escribe un caracter-> ")
 
vocales = [a, e, i, o, u]:
    
if caracter == a:
    
elif caracter == e:
    print("Es una vocal")
elif caracter == i:
    print("Es una vocal")
elif caracter == o:
    print("Es una vocal")
elif caracter == u:            
    print("Es una vocal")
else:
    print("no es vocal")'''
# solucion

letra = input("Introduzca un caracter-> ").lower()   #.lower() lo convierte en minuscula simpre poner los parentesis()

if letra == 'a' or letra =='e' or letra =='i' or letra == 'o' or letra =='u':
    print("Es una vocal")
else:
    print("No es una vocal")