# como convertir variables locales, en variables globales
'''
def suma(a,b):
    resultado = a+b
    print(resultado)
    return resultado

# para que el return funcione, tenemos que crear una variable fuera del scope, 
# para que almacene la infomacion, y no hace falta que se llame igual, yo le puesto resultado2
    
resultado2 = suma(5,6)
print(resultado2)
# para imprimirla si tenemos que llamar a la variable, esta claro, sino no imprimimos nada
# esta es la variable anterior de resultado, 
# pero al estar fuera de la funcion de arriba hay no significa nada
'''
# OTRO EJEMPLO CON MAS VARIABLES
def operaciones(a,b):
    sumar = a+b
    restar = a-b
    multiplicar = a*b
    return sumar, restar, multiplicar

s,m,r = operaciones(10,8)
print(s,m,r)

