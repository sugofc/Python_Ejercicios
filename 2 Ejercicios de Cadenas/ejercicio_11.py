"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades.
Muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""
producto = 'Ceramica' #input("Nombre Producto: ")
precio = 2_500 #int(input("Precio Producto: "))
cantidad = 3 ##int(input("Cantidad Producto: "))

print("{}: {} unidades x ${:.2f} = {:.2f}".format(producto,cantidad,precio,precio*cantidad))
print(f"{producto}: {cantidad} unidades x ${precio:.2f} = {precio*cantidad:.2f}")