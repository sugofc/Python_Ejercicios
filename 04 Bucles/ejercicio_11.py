"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

palabra = 'murcielago'

for i in range(len(palabra),0,-1):
    print(palabra[i-1])