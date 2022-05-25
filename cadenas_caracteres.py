''' Cadena de caracteres
cadena = 'hola mundo'
print(cadena)
cadena = "hola mundo"
print(cadena)'''

# se pueden usar los dos tipos de comillas
# para poner comillas dentro de comillas
cadena = "estoy 'estudiando' no molestes"
print(cadena) #Salida terminal   estoy 'estudiando' no molestes
# y si queremos poner comillas dobles en las dos partes? 
frase = "estoy \"estudiando\"no molestes" # esta seria la forma de hacerlo \
print(frase)
'''el simbolo \ tiene sus opciones visuales 
por ejemplo
\t hace una tabulacion
\n hace un salto de linea
que pasa si por ejemplo queremos que se grabe el texto en crudo ejemplo
ponemos uns direccion de ordenador
d:\nombre\trabajo -> tendriamos un problema porque haria un salto de linea y una tabulacion
para solucionar ese problema se pone un r antes de esta manera r"d:\nombre\trabajo"
asi lo graba en crudo y no la va a procesar ejemplo
'''
archivo = "d:\nombre\trabajo"
print(archivo)
'''SALIDA TERMINAL
d:
ombre   rabajo
'''
archivo = r"d:\nombre\trabajo"
print(archivo) #SALIDA TERMINAL d:\nombre\trabajo

#===========================================================================================#
# construir cadenas de varias lineas
# para eso usamos """ """ 3 dobles comillas ejemplo
cadena = ("""
hola que tal?
como estas? 
como ha ido el dia?
""")
print(cadena)

'''SALIDA TERMINAL
hola que tal?
como estas? 
como ha ido el dia? '''
# tambien se puede imprimir de esa manera dentro del print ejemplo
print("""
hola que tal?
como estas? 
como ha ido el dia?
""")
# y tendria la misma salida que arriba
#===========================================================================================#
cadena1 = "hola "
cadena2 = "que tal"
print (cadena1+cadena2) # SALIDA TERMINAL hola que tal

cadena = "Alejandro"
print(cadena[0]) # para imprimir cualquier indice tambien se cumplen los negativos [-1]
cadena = "Alejandro"
print(cadena[0:4]) #tb se puede hacer slicing que es imprimir de un indice hasta otro
# LAS CADENAS DE CARACTERES CON INMUTABLES
# pero se pueden modificar de varias formas, una es esta
cadena = "Alejandro"
cadena = 'a' + cadena[1:] # le estamos diciendo que ponga a y
#luego concatenamos la cadena desde el indice 1 que es la l SALIDA TERMINAL cadena = "alejandro"
# se pueden contar los caracteres con el metodo len;   print(len(cadena))
# metodos de trabajo con cadenas

cadena = "hola mundo".upper() # este metodo te convierte la cadena a mayusculas se puede usar en la variable o en el print
cadena = "hola mundo".lower() # este metodo te convierte la cadena a minuscula se puede usar en la variable o en el print
cadena = "hola mundo".capitalize() # este metodo te convierte a mayusculas la primera letra igual en print
cadena = "hola mundo".title() # este metodo te convierte la primera letra de cada palabra en mayusculas igual en print
cadena = "hola mundo".count('o') # este metodo cuenta los elementos
cadena = "hola mundo".count('mundo') # este metodo cuenta tambien las palabras
cadena = "hola mundo".find("h") # te busca palabra o caracter, y te indica el indice que esta
cadena = "hola mundo".rfind("h") # esto busca la ultima coincidencia ejemplo
#si buscamos mundo find dira que esta en el indice 5 que es donde empieza la palabra
# si lo buscamos con rfind(reversefind) nos dira en que indice acaba la palabra mundo
cadena = "1000".isdigit() # entrega un booleano, aunque sea cadena detecta numeros
cadena = "1000".isalpha() # entrega un booleano, esto busca si es alfabetico o no
cadena = "1000".isalnum() # este metodo igual, entrega true o false si la cadena es alfanumerica
cadena = "hola mundo".islower() # esto detecta si es todo en minuscula, y entrega un booleano 
cadena = "hola mundo".isupper() # igual pero en mayusculas
cadena = "hola mundo".istitle() # comprueba si es un titulo, es decir, si la primera letra esta en mayus
cadena = "hola mundo".isspace() # comprueba si esta todo espacios la cadena y devuelve un true o false
cadena = "hola mundo".startswith('h') #entrega valor booleano, si la cadena comienza con('h') sera true xk empieza por h
cadena = "hola mundo".endswith('o') #entrega valor booleano, si la cadena empieza con('o') sera true xk termina por o
cadena = "hola mundo".split() # separa los elementos de la cadena si encuentra un espacio
cadena = "hola-mundo".split('-') # ahora le damos el parametro - y actua como split()
cadena = ",".join('alejadnro') #mete el simbolo que le indiquemos en este caso "," entre los elementos de la cadena
cadena = "     hola mundo      ".strip()# elimina espacios innecesarios
cadena = " ....hola mundo....".strip(".") # si le pasamos un parametro a strip, lo eliminara de la cadena
cadena = "hola mundo".replace("a", "4") #remplaza lo que intoduzcamos primero, por lo segundo, ejemplo a por 4: hol4 mundo
print(cadena)
