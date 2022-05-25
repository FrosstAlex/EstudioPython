# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos y por ultimo muestre la lista
'''
comedor_casa = ["piano", "mesa", "sofa", "piano", "taburete", "tv", "estufa", "mesa", "piano"]
print(comedor_casa)
comedor_casa.pop(0)
comedor_casa.pop(1)
comedor_casa.pop(3)
print(comedor_casa)
'''
# solucion
comedor_casa = ["piano", "mesa", "sofa", 3, "taburete", "tv", "estufa", 3, "mesa", "piano"]
# la solucion es convertir la lista en conjunto
conjunto_casa = set(comedor_casa)
print(conjunto_casa)
# y ahora volverla otra vez una lista
comedor_casa = list(conjunto_casa)
print(comedor_casa)
# Salida terminal {3, 'estufa', 'piano', 'taburete', 'mesa', 'sofa', 'tv'} conjunto
# Salida terminal [3, 'estufa', 'piano', 'taburete', 'mesa', 'sofa', 'tv'] lista

# otra forma
comedor_casa = ["piano", "mesa", "sofa", 3, "taburete", "tv", "estufa", 3, "mesa", "piano"]
comedor_casa = list(set(comedor_casa))
print(comedor_casa)


