"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

for i in range(1,11):
    for k in range(1,11):
        print(f"{i}x{k}={i*k}", end='\t')
    print('')