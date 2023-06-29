"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
nums = list()

while True:
    nums.append(int(input("Ingrese Numero: ")))
    s = input("Escriba S para salir o M para mostrar: ")
    if s.lower() == 's':
        break
    elif s == 'm':
        nums.sort()
        print(nums)
        break