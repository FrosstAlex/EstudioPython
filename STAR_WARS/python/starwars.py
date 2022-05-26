# programa creado para ver la historia de los personajes de star wars
'''
tiene k haber un menu con las opciones
1.- Listar los personajes
2.- Elegir personajes
3.- Modificar personajes
4.- Añadir personajes
5.- Salir

personaje 1...
Nombre: Darth Vader 
Especie: Humano
Padres: Nacido de la fuerza
Hijos: Luke y Leia Skywalker
Edad: Desconocida
Muerte: Salvando a su hijo
'''
class personajes():
    def personaje(self):
        self.nombre = "Goku"
        self.raza = "Humano"
        self.padres = "SonGoanda Abuelo"
        self.hijos = "Son Gohan"
             
    while True:
        print("\t************")
        print("\t STARS WARS")
        print("\t************")
        print("""
        1.- Listar los personajes
        2.- Elegir personajes
        3.- Modificar personajes
        4.- Añadir personajes
        5.- Salir
              """)
    
        opcion = (input("Seleccione una opcion-> "))
        if opcion == "1":
            print(personaje)
            break