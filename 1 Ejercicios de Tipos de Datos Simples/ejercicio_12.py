"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

pan = int(input("Cantidad de PAN que no es del día: "))
costo_pan = 3.49
dcto_pan = 0.6
total_dcto_pan = ((pan * costo_pan) * (1 - dcto_pan))

print(f"""\nEl coste del pan fresco es de: {costo_pan}€.
El descuesto sobre el pan que no es fresco es de: {dcto_pan*100}% -> {dcto_pan}.
El costo final a pagar es de: {round(total_dcto_pan,2)}€.
Si fuera pan fresco, el valor seria: {round(pan*costo_pan,2)}€""")