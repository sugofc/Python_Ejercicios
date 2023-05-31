"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
Formula: IMC = peso (kg) / (altura (m))^2
"""

kg = int(input("Peso en Kilos: "))
mt = float(input("Estatura en Metros: "))
imc = kg/(mt)**2

print(f"Peso es {kg} Kilogramos\nEstatura es de {mt} Metros\nIMC es de {imc}")