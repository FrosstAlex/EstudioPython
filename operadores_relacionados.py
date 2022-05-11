'''
se utilizan para establecer una relacion entre 2 valores.
compara estos valores entre si y 
esta comparacion produce un resultado booleano (True,False)
tienen el mismo nivel de prioridad de evaluacion
los operadores relacionados tienen menos prioridad que los aritmeticos
son los siguientes:
< menor que
> mayor que
>= mayor o igual que
<= menor o igual que
!= diferente que
== igual que
'''
# ejemplo

resultado = 10 != 20
print (resultado)

# quiero comprobar si a + b es igual a c
a = 10
b = 20
c = 30
resultado = a+b == c
print(resultado)

a = "alex"
b = "maricarmen"
c = "alma"
resultado = a+b == c
print(resultado)

# salida terminal
'''
True
True
False
'''