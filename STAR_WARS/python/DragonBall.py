# programa creado para ver la historia de los personajes de Bolla del Dragon
'''
tiene k haber un menu con las opciones
1.- Listar los personajes
2.- Elegir personajes
3.- Modificar personajes
4.- Añadir personajes
5.- Salir

personaje 1...
Nombre: Son Goku 
Especie: Humano
Padres: Abuelo Son Gohanda
Hijos: Son Gohan
Edad: Desconocida
Muerte: Aun no a muerto
'''
class Personajes():
    def __init__ (self):
        self.nombre = None
        self.raza = None
        self.padres = None
        self.hijos = None
# Metodos
    def __init__(self):
        self.ataques
        self.personalidad
        self.transformacion
             
    while True:
        print("\t*************")
        print("\t DRAGON BALL")
        print("\t*************")
        print("""
        1.- Listar los personajes
        2.- Elegir personajes
        3.- Modificar personajes
        4.- Añadir personajes
        5.- Salir
              """)
    
        opcion = (input("Seleccione una opcion-> "))
        if opcion == "1":
            print()
            break