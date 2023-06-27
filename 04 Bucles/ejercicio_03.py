"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

num = 10
for i in range(1,num+1):
    if i % 2 != 0:
        print(i, end=', ')

print("\n")

num = 10
for i in range(1,num+1,2):
    print(i, end=', ')