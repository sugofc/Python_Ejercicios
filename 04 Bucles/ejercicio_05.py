"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

monto = 1000
years = 5
interes = 10

for i in range(1,years+1):
    inversion = monto * interes / 100
    monto += inversion
    print(f"Monto tras el año {i}: {monto} - Interes Ganado: {inversion}")