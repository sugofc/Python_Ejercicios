"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

frase = "Pedrito clavo un clavito, que clavito clavo Pedrito"
letra = 'a'
cantidad = 0

for i in range(len(frase)):
    if str(frase[i]).lower() == letra.lower():
        cantidad += 1
else:
    print(f"La letra {letra} esta {cantidad} veces")