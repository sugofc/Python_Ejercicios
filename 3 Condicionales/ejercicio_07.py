"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	                Tipo impositivo
Menos de $100000	          5%
Entre $100000 y $200000	     15%
Entre $200000 y $350000      20%
Entre $350000 y $600000      30%
Más de $600000	             45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""

renta_anual = 350_001

if renta_anual > 600_000:
    print(f"Renta Anual: {renta_anual} -> 45% -> {renta_anual*0.45}")
elif renta_anual > 350_000:
    print(f"Renta Anual: {renta_anual} -> 30% -> {renta_anual*0.3}")
elif renta_anual > 200_000:
    print(f"Renta Anual: {renta_anual} -> 20% -> {renta_anual*0.2}")
elif renta_anual > 100_000:
    print(f"Renta Anual: {renta_anual} -> 15% -> {renta_anual*0.15}")
else:
    print(f"Renta Anual: {renta_anual} -> 5% -> {renta_anual*0.05}")
    