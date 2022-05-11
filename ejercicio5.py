'''
Ejericio5
En una tienda ofrecen el 15% de descuento y el cliente desea
saber el precio que va a pagar

# Resolucion
precio = float(input("Introduce el precio total del precio-> "))
descuento = precio * 0.15
precio_final = precio - descuento

print(f"El precio final a pagar es de {precio_final:.2f}€")
'''

# Resolucion mia
precio = float(input("Introduce el precio total del precio-> "))
porcentaje_descuento = float(input("introduce el descuento-> "))
descuento = precio * porcentaje_descuento /100
precio_final = precio - descuento
print(f"El precio final a pagar es de {precio_final:.2f}€")

