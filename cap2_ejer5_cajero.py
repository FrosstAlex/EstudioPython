'''
hacer un programa que simule un cajero automatico con un saldo inicial de 1000€ y tendra el siguiente menu
1.- ingrasar dinero
2.- retirar dinero
3.- mostrar dinero disponible
4.- salir
'''
#mi solucion

# Solucion
saldo = 1000
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
      print(f"Dinero disponible en cuenta {saldo}€")
elif opcion == 3:
    print(f"Su saldo es de->{saldo}€")
elif opcion == 4:
    print("Saliendo...")
else:
    print(" error: elija una opcion disponible")
    