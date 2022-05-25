'''
Hacer un programa donde el usuario introduzca una frase, 
se le devolvera la misma frase pero sin espacios en blanco y 
ademasun contador de cuantos caracteres tiene la frase
(sin contar los espacios en blanco)
'''
'''
frase = (input("Introduzca la frase deseada->"))
frase = list(frase)
frase.remove(" ")
frase.count(frase)
print(frase)'''

#Solucion

frase = (input("Introduzca la frase->"))
frase2 = ""

for i in frase:
    if i != " ":    # esto es que 
        frase2 += i # += en estas situaciones es concatenar o añadir
                    # en frase 2 estamos añadiendo la salida del if 
frase = frase2
print(f"\nFrase final {frase}")
print(f"Nº de caracteres :{len(frase)}")
