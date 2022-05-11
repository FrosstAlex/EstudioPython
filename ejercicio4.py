'''
hacer un programa para ingresar el radio de un circulo y se reporte su area 
y la longitud de la circunferencia
'''

# respuesta correcta
import math

radio = float (input("radio ->"))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"El area es:{area:.2f} ")
print(f"la longitud es: {longitud:.3f}")