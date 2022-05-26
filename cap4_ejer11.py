'''
Hacer un programa que simule una agenda de contactos
crear un diccionario donde la clave sea
el nombre y el valor el telefono, el programa tendra el siguiente menu
1.- Nuevo contacto
2.- Borrar contacto
3.- Ver contactos existentes
4.- Salir
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
agenda = {}

while True:
    print("\t========")
    print("\t.:Menu:.")
    print("\t========")
    print("1.- Nuevo contacto")
    print("2.- Borrar contacto")
    print("3.- Ver contactos existentes")
    print("4.- Salir")
    menu = int(input("Seleccione una opcion"))
    
    print() #salto de linea
    
    if menu == 1:
        agenda = str(input("Inroduzca nombre y telefono"))  
        agenda[""]= ""
        print(f"\nSu agenda es {agenda.items}")
    elif menu == 2:
        print("Borrar contacto")
        agenda = input("Inroduzca nombre") [""]= "" 
        del(agenda)["{}"]
    elif menu == 3:
        print("Ver contactos")
        agenda.items
        print(agenda)
    elif menu == 4:
        print("saliendo...")
        break
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
no se como introducir datos dentro del diccionario 

agenda = {}

while True:
    print("\t========")
    print("\t.:Menu:.")
    print("\t========")
    print("1.- Nuevo contacto")
    print("2.- Borrar contacto")
    print("3.- Ver contactos existentes")
    print("4.- Salir")
    menu = int(input("Seleccione una opcion->"))
    
    print() #salto de linea
    if menu == 1:
       nombre = input("Inroduzca nombre->")
       telefono = input("Introduzca el telefono->")
       
       else:
           print("Contacto existente...")
    elif menu == 2:
        nombre = input("Elija el contacto a borrar->")
        del agenda[nombre]
        print("Contacto borrado!!")
    elif menu == 3:
        print(agenda)
    elif menu == 4:
        print("Saliendo....")
        break
'''
#Solucion

agenda = {}

while True:
    print("\t========")
    print("\t.:Menu:.")
    print("\t========")
    print("1.- Nuevo contacto")
    print("2.- Borrar contacto")
    print("3.- Ver contactos existentes")
    print("4.- Salir")
    menu = int(input("Seleccione una opcion->"))
    
    print() #salto de linea
    if menu == 1:
       nombre = input("Inroduzca nombre->")
       telefono = input("Introduzca el telefono->")
       edad = input("introduzca la edad->")
       sexo = input("introduzca el sexo->")
       
       if nombre not in agenda:
           agenda[nombre] = telefono
           agenda[edad] = sexo
           print("Contacto agregado!!")                          
       else:
           print("Contacto existente...")
           
    elif menu == 2:
        nombre = input("Inroduzca nombre->")
        if nombre in agenda:
            del(agenda[nombre])
            print("Contacto borrado...")
        else:
            print("Ese contacto no existe")
    
    elif menu == 3:
        print("Agenda de contactos")
        for nombre, telefono in agenda.items():
            print(f"Nombre{nombre} Telefono{telefono}")
            
    
    elif menu == 4:
        print("Saliendo de agenda...")
        break
    else:
        print("Opcion equivocada, elija otra")        