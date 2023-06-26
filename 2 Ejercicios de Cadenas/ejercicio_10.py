"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""

cesta = 'leche,huevos,palta,azucar' #input("Liste sus productos separados por coma: ")

print("\nForma 1")
cesta = cesta.replace(',','\n')
print(cesta)

print("\nForma 2")
cesta = 'leche,huevos,palta,azucar' #input("Liste sus productos separados por coma: ")
cesta = "\n".join(cesta.split(','))
print(cesta)