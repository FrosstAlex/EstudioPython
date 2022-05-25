# cajero automatico con bucle
'''
hacer un programa que simule un cajero automatico con un saldo inicial de 1000€
y tendra el siguiente menu de opciones 
1.-Ingresar dinero
2.-Retirar dinero
3.-Mostrar saldo cuenta
4.-Salir

MI SOLUCION, CASI PERO NO TAN DEPURADA SI HUBIERA PENSAO UN POCO MAS...
print("\t============================")
print("\tCajero automatico con bucles")
print("\t============================")
saldo = 1000
while True:
    print("\t.:Menu:.")
    print("1.-Ingresar dinero")
    print("2.-Retirar dinero")
    print("3.-Mostrar saldo cuenta")
    print("4.-Salir")
    menu = int(input("\nSeleccione una opcion->"))


    if menu == 1 or menu ==2 or menu ==3 or menu ==4:
        if menu ==1:
            ingresar = int(input("Indique cantidad a ingresar->"))
            print(f"Su saldo es de {saldo + ingresar}")
        elif menu == 2:
            retirar = int(input("Indique cantidad a retirar->"))
            print(f"Su saldo es de {saldo - retirar} ") 
        elif menu == 3:
            print(f"Su saldo es de {saldo} ")
        else:
            menu == 4
            print("Saliendo....")
            break
            '''
# Solucion
saldo = 1000
while True:# El bucle va despues, sino cuando se cambia la cantidad, al empezar el bucle el saldo volveria a 1000
    print("\t .:Menu:.")
    print("1.- ingrasar dinero")
    print("2.- retirar dinero")
    print("3.- mostrar dinero disponible")
    print("4.- salir")
    opcion = int(input(" Elija una opcion: "))

    print()

    if opcion == 1:
        extra = float(input("Cuanto dinero desea ingresar-> "))
        saldo += extra
        print( f"Dinero disponible en cuenta {saldo}€")

    elif opcion == 2:
      retirar = float(input("Cuanto dinero desesa retirar-> "))
      if retirar>saldo:
            print("No disponible")
      else:
          saldo-= retirar
          print(f"Dinero disponible en cuenta {saldo } €")
          
    elif opcion == 3:
        print(f"Su saldo es de->{saldo}€")
    elif opcion == 4:
        
        print("Saliendo...")
        break
    else:
        print(" error: elija una opcion disponible")
        
print() # hace un salto de linea
    
