"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
precio = input("Precio del producto en €: ")

print(f"El precio es de {precio}, son {precio[:precio.rfind('.')]}€ y son {precio[precio.rfind('.')+1:]} centimos")