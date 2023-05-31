"""
Escribir un programa que lea un entero positivo, "N", introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta "N".
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
suma = n(n+2)/2
"""

n = int(input("Ingrese numero: "))
suma = int(n*(n+1)/2)

print(f"la suma desde el 1 hasta el {n} es {suma}")