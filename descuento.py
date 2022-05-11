# programa para hacer descuentos

precio = float(input("ponga el precio total>: "))

descuento = precio * float(input("ponga el porcentaje de descuento>: ")) /100

precio_final = precio - descuento

print(f"El precio final es>: {precio_final:.2f}€")