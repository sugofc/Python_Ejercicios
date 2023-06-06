"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

## Con datos Juntos
# fecha = "24/10/1987"

# print(f"""
# Dia: {fecha[:2]}
# Mes: {fecha[3:5]}
# Año: {fecha[6:]}
# """)


## Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha = "24/10/1987"

day = fecha[:fecha.find("/")]
var = fecha[fecha.find("/")+1:]
month = var[:var.find("/")]
year = var[var.find("/")+1:]
print(f"""
Dia: {day}
Mes: {month}
Año: {year}
""")



## Con Datos Separados
# import datetime as dt

# d = 24 #int(input(Ingrese Dia (Numero): ))
# m = 10 #int(input(Ingrese Mes (Numero): ))
# a = 1987 #int(input(Ingrese Año (Numero): ))

# fecha = dt.datetime(a,m,d)
# fecha_format = fecha.strftime("%d/%m/%Y")

# print(fecha_format)