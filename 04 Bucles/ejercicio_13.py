"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

while True:
    eco = input("Escriba una palabra: ")
    if eco.lower() == 'salir':
        break
    else:
        print(eco)