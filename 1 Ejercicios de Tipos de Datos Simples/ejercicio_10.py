"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

payasos = int(input("Cantidad de Payasos: "))
muñecas = int(input("Cantidad de Muñecas: "))
peso_payaso = payasos*112
peso_muñeca = muñecas*75

print(f"""\nPayasos Vendidos {payasos} - {peso_payaso} gramos
Muñecas Vendidas {muñecas} - {peso_muñeca} gramos
Total de gramos {peso_payaso+peso_muñeca}
Total de kg {(peso_payaso+peso_muñeca)/100}""")