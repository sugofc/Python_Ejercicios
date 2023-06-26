"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de $24.000 multiplicada por la puntuación del nivel. (nivel 1: 1.X, nivel 3: 3.X)

Nivel	        Puntuación
Inaceptable	       0.0
Aceptable	       0.4
Meritorio	       0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""

bonus = 20_400
puntos = 0.8
niv = str()

if puntos == 0.0:
    niv = 'Inaceptable'
elif puntos == 0.4:
    niv == 'Aceptable'
elif puntos >= 0.6:
    niv = 'Meritorio'

print("Tu nivel de rendimiento es %s" % niv)
print("Te corresponde cobrar $%.2f" % (puntos * bonus))