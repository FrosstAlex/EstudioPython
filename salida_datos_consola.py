# Salidas
# Forma 1
nombre = ("Alejandro")
edad = 39

print("hola", nombre, "tienes", edad, "años")

# Forma 2 mas facil de usar

nombre = ("Alejandro")
edad = 39
print(f"hola{nombre} tienes {edad}")

# introduciendo datos
nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))
print(f"hola {nombre} tienes {edad} años")


# Forma 3 
nombre = ("Alejandro")
edad = 39
print("hola {} tienes {} años".format(nombre,edad))

# Prueba mia, para introduccion de datos, se pueden añadir los campos que se quieran tlf,direccion
nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))

print("hola {} tienes {} años".format(nombre,edad))




