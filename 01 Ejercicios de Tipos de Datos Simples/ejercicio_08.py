"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""

n = int(input("n1: "))
m = int(input("n2: "))
r = n%m
c = n//m

print(f"\nNumeros introducidos son {n} y {m}, cuociente es {c} y resto es {r}")