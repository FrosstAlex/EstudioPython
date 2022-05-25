'''
Escriba un programa donde cree una lista con los siguientes 
personajes del señor de los anillos

nombre:aragorn
clase guerrero
raza:dunadan del norte

nombre:legolas
clase:arquero
raza:elfo sindar

nombre:gandalf
clase:mago
raza:istar
'''
'''anillos = {"nombre":"Aragorn",}
p0 = {"Nombre":"Aragorn", "Clase":"Guerrero", "Raza":"Dúnadan del Norte" }
p1 = {"Nombre":"Legolas", "Clase":"Arquero", "Raza":"Elfo Sindar"}
p2 = {"Nombre":"Gandalf", "Clase":"Mago", "Raza":"Istar"}
# Pasandolo a lista
pj0 = list(p0)
pj1 = list(p1)
pj2 = list(p2)
print(pj0, pj1, pj2)
TERMINAL ['Nombre', 'Clase', 'Raza'] ['Nombre', 'Clase', 'Raza'] ['Nombre', 'Clase', 'Raza']'''



# Solucion
personajes = []
p0 = {"Nombre":"Aragorn", "Clase":"Guerrero", "Raza":"Dúnadan del Norte" }
p1 = {"Nombre":"Legolas", "Clase":"Arquero", "Raza":"Elfo Sindar"}
p2 = {"Nombre":"Gandalf", "Clase":"Mago", "Raza":"Istar"}
personajes.append(p0) # Agregamos personajes a la lista
personajes.append(p1)
personajes.append(p2)
print (len(personajes)) #imprime cuantos elementos tiene una lista
print (personajes [2]) #imprime los elementos por separado de una lista