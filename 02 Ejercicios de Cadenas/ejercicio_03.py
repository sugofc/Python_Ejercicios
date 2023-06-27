"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""
n = 0

nombre = "Felipe Castillo" #input("Escriba su nombre: ")

for i in nombre:
    n += 1

print(f"El nombre {nombre.upper()} tiene {len(nombre)} letras.")