'''
todas las clases tiene cualidades
atributos y acciones
que puede hacer por ejemplo de perro
atributos
tamaño, color, raza, edad unos son permanentes y otros cambiantes
acciones 
ladrar, jugar, correr, comer
todos tienen lo mismo pero no son iguales, por ejemplo todos tienen tamaño, pero no todos el mismo tamaño
comparten atributos y acciones aunque no sean exactamente iguales
la clase PERRO es la que rejunta todas las posibles cualidades y acciones que puede realizar un objeto
perro en particular. 
un objeto es cada perro especifico, por ejemplo, tommy el dalmata
un ejemplo con coches
todos tienen 4 ruedas(pero no todas las ruedas son iguales), todos tienen ventanas(pero no son todas iguales)
'''
#sintaxis

from mailbox import NoSuchMailboxError


class Perro: # buenas practicas es escribir la primera letra mayuscula de una clase
    #constructor
    def __init__(self):
        #atributos
        self.tamaño = None
        self.edad = 0
        self.color = None
        self.raza = None
        self.nombre = None
        
    #metodos
    def ladrar(self):
        print("EL perro esta ladrando")
        
    def comer(self):
        print("El perro esta comiendo")
        
    def jugar(self):
        print("El perro esta jugando")
    def cambiar_nombre(self, nombre):
        self.nombre = nombre
        
#instancia run objeto
mi_perro = Perro()
mi_perro.comer
print("Mi perro esta comiendo")
mi_perro.jugar
print("Mi perro esta jugando")
mi_perro.cambiar_nombre("Tina")
print(f"El perro ahora se llama {mi_perro.nombre} ")
    
    