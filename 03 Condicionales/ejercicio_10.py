"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

veg = 'Pimienta, Tofu'
notveg = 'Peperoni, Jamón, Salmón'

print("1) Vegana\n2) No Vegana\n")
opcpiz = int(input('Elija una opcion: '))

if opcpiz == 1: # Pizza Vegana
    print(f"1) {veg[:8]}\t2) {veg[8+2:]}")
    opcing = int(input('\nElija una opcion: '))
    if opcing == 1:
        print(f"Su pizza contiene: Mozzarella, Tomate, {veg[:8]}")
    else:
        print(f"Su pizza contiene: Mozzarella, Tomate, {veg[8+2:]}")
else: # Pizza No Vegana
    print(f"1) {notveg[:8]}\t2) {notveg[8+2:15]}\t3) {notveg[17:]}")
    opcing = int(input('Elija una opcion: '))
    if opcing == 1:
        print(f"Su pizza contiene: Mozzarella, Tomate, {notveg[:8]}")
    elif opcing == 2:
        print(f"Su pizza contiene: Mozzarella, Tomate, {notveg[8+2:15]}")
    else:
        print(f"Su pizza contiene: Mozzarella, Tomate, {notveg[17:]}")