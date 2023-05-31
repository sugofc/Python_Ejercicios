"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

inversion = float(input("Cantidad a Invertir: "))
interes = float(input("Interes Anual: "))
num_years = int(input("Numero de Años: "))
capital = round(inversion * (interes / 100 +1) ** num_years,2)

print(f"\nInversion: {inversion}\nInteres Anual: {interes}\nCantidad Años: {num_years}\nCapital Final: {capital}")