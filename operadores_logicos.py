'''
permite construir expresiones logicas
se obtiene como resultado un valor booleano

And(conjuncion) and
Or(disyuccion)  or
Not(negacion)   not
se escriben en minuscula
PROPIEDAD OPERADORES LOGICOS
primero se evalua 
not 
and 
or
en ese orden
'''
a = 10
b = 12
c = 13
d = 10
print((a>b)or(a<c))and((a==c)or(a>=b))
#        F or T    and     F or F
#           T       and        F
#                  Falso
print (True and False)
'''
operador and se conoce como multiplicacion logica
operando1 operador operando2 resultado
  true      and      true      true
  true      and      true      false
  false     and      true      false
  false     and      true      false
'''
'''
operador or se conoce como suma logica
operando1 operador operando2 resultado
  true      and      true      true
  true      and      false     true
  false     and      true      true
  false     and      false     false
'''
'''
operador not se conoce como operador de negacion
  operando   resultado
  not(true)  false      
  not(false) true           
'''
'''
prioridad operaciones generales
1.- ()
2.- **
3.- * / % not
4.- + - and
5.- < > == >= <= != or
'''
# ejemplo
a = 10
b = 15
c = 20
resultado = not((a>b) or (b<c))
print(resultado)