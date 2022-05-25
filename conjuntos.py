'''Conjuntos son grupos de elementos desordenados, dentro de los conjuntos no puede haber otro
tipo de colecciones, ni listas, ni tuplas ni nada pero si admite todo tipo de datos, str, int, float, booleano,
no pueden valer valores duplicados, son valores unicos
SINTAXIS
comedor = set()
comedor = {}
print(comedor)
MUY IMPORTANTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
LOS CONJUNTOS USAN LLAVES, COMO LOS DICCIONARIOS
CON LA PRIMERA LINEA ESPECIFICAMOS QUE ES UN CONJUNTO Y NO UN DICCIONARIO
comedor = set() siempre y cuando se cree un conjunto vacio, sino se puede crear normal
IMPORTANTISIIMOOO!!!!!!!!!
'''
comedor = set() # como es una funcion de activa con ()
comedor = {"mesa", "sillas", 2, "sofas", 3, "piano","mesa", "sillas"}
print(comedor)
comedor.add(2.3)
print(comedor)
'''
SALIDA TERMINAL
{2, 3, 'sofas', 'sillas', 2.3, 'mesa', 'piano'}
COMO SE COMPRUEBA, NO SE REPITEN NI MESA NI SILLAS
'''
# para eliminar elementos de un conjunto

comedor = set() # como es una funcion de activa con ()
comedor = {"mesa", "sillas", 2, "sofas", 3, "piano","mesa", "sillas"}
print(comedor)
comedor.discard("sillas")
print(comedor)
'''salida terminal {2, 3, 'sofas', 'piano', 'mesa'} para vaciar por completo el conjunto tambien se usa .clear()
tambien se puede buscar como en listas y tuplas
'''
# conjuntos parte 2

a = {1,2,3}
b = {3,2,1}
# c = a + b no se pueden sumar conjuntos con + para sumarlos se usa | ejemplo c = a | b
# c = a & b para sacar la interseccion de dos conjuntos
# c = a - b diferencia de conjuntos solo saca los elementos diferentes de cada conjunto
# c = a ^ b diferencia simetrica de conjuntos solo saca los elementos diferentes de los dos conjuntos
print(a == b) # devuelve un booleano, con True, ya que son los mismos elementos, aunque esten desordenados

# como saber si un conjunto es subconjunto de otro

a = {1,2,3}
b = {4,5,6}
c = {1,2,3,4,5,6}
print(a.issubset(c)) # con issubset salida terminal: True, me dice que si, es subconjunto
# deben estar todos los elementos para se subconjunto
# tambien se puede ver si es superconjunto de con issuperset ejemplo.... respuesta True xk contiene todos los elementos de a
print(c.issuperset(a))
# tambien podemos ver si son disconexos los conjuntos con isdisjoin.... ejemplo, respeusta True xk no contiene lo mismo
print(a.isdisjoint(b))

# conjunto inmutable, para eso se usa la funcion frozenset ejemplo
a = frozenset({1,2,3}) # sintaxis