"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

nom = input("Digite Nombre: ")
n = int(input("Cantidad de veces que quiere que se repita el nombre: "))

print((nom + "\n") * int(n))