"""
Para tributar un determinado impuesto se debe ser mayor o igual a 18 años y tener unos ingresos iguales o superiores a $100000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

edad = 20
ingresos = 300000

if edad >= 18 and ingresos >= 100_000:
    print("Puede Tributar")
else:
    print("NO Puede Tributar")
