"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""

import string

abc = list(string.ascii_lowercase)
abc_ok = list()

for l in range(1,len(abc)+1):
    if l % 3 != 0:
        abc_ok.append(abc[l-1])
else:
    print(abc_ok)
