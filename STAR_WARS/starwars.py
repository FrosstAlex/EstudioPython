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
agenda = {"alejandro":{"edad":39,"estatura":1.70}}, {"conchi":[37, 1.60]},{"jony":[39, 1.75]}#un dic dentro de otro
print(agenda)'''


#personaje = {"Darth Vader":{"Especie":"Humano", "Padre":"nacido de la fuerza", "hijos":"Luke y Leia skywalker"}

personajes = "Darth Vader", "Leia Skywalker", "Luke Skywalker"
darthvader = {"Darth Vader":
    {"Especie":"Humano",
     "Padre":"nacido de la fuerza",
     "hijos":"Luke y Leia skywalker"}}
leia = ("Leia",
     "Especie","Humana",
     "Padre","Anakin Skywalker",
     "hijo","Kylo Ren")
luke = {"Luke":
    {"Especie":"Humano",
     "padre":"Anakin Skywalker",
     "hijos":"no se le conoce ninguno/a"}}
while True:
    print("\t************")
    print("\t STARS WARS")
    print("\t************")
    print("""
    1.- Listar los personajes
    2.- Elegir personaje
    3.- Modificar personaje
    4.- Añadir personaje
    5.- Salir
          """)
    print()
    opcion = (input("Seleccione una opcion-> "))
    if opcion == "1":
        print(personajes)
        
    elif opcion == "2":
        pj = input("Seleccione un personaje->")
        if pj == "darth vader":
            print(darthvader)
        elif pj == "leia":
            print(leia)
        elif pj == "luke":
            print(luke)
    elif opcion == "5":
        break
    print()