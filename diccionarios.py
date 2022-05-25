# discionarios sintaxis 
# diccionario = {}  
# print(diccionario)

'''traduccion = {"blue":"azul", "green":"verde", "red":"rojo"}
print(traduccion)
# para imprimir solo un valor, hay que poner la clave clave:valor
#print(traduccion["blue"])

traduccion = {"blue":"azul", "green":"verde", "red":"rojo"}
#para agregar un elemento directamente la sintaxis es la siguiente
traduccion["amarillo"] = "yellow"

# para agregar con input
       nombre = input("Inroduzca nombre->")           creas variable nombre
       telefono = input("Introduzca el telefono->")   creas variable telefono
       
       if nombre not in agenda:                       
           agenda[nombre] = telefono                  y metes las variables para que las agrege
           print("Contacto agregado!!")


#para modificar es igual
traduccion["blue"] = "AZUL" #modificado a mayusculas
print(traduccion)

# para borrar un determinado elemento
del(traduccion)["green"]
print(traduccion)

agenda = {"alejandro":{"edad":39,"estatura":1.70}}, {"conchi":[37, 1.60]},{"jony":[39, 1.75]}#un dic dentro de otro
print(agenda)'''

# Diccionarios 2 prueba real de diccionario con nombres inventados
'''
cosas = {"informatica":("app", "miSoftware", "tomselectro")}, {10:"paulo"}, {7:"cristiano"}
print(cosas[10])

equipo = {10:"paulo", 7:"cristiano", 11:"douglas"}
print(equipo[10])
cosas = {"informatica":("app", "miSoftware", "tomselectro"), 10:"paulo", 7:"cristiano"}
print(cosas["informatica"])
para controlar los fallos si no sabes si hay alguna clave en el diccionario, y no hacer
que el programa se detenga, se puede hacer de la siguiente manera
'''

f1team = {14:"Fernando Alonso", 1:"Max Verstappen", 16:"Charles Leclerc", 55: "Carlos Sainz"}
print(f1team.get(10, "no existe este piloto"))
#tambien se puede buscar atraves de in
print(55 in f1team) # me retorna un True xk es verdasd que esta
#forma de ver todas las claves del diccionario
print(f1team.keys()) # terminal: dict_keys([14, 1, 16, 55])
# y para ver el valor de las claves se usa
print(f1team.values()) # retorna: dict_values(['Fernando Alonso', 'Max Verstappen', 'Charles Leclerc', 'Carlos Sainz'])
# tambien se puede ver de esta manera
print(f1team.items())
#Terminal dict_items([(14, 'Fernando Alonso'), (1, 'Max Verstappen'), (16, 'Charles Leclerc'), (55, 'Carlos Sainz')])
#para borrar el contenido de un diccionario
# f1team.clear