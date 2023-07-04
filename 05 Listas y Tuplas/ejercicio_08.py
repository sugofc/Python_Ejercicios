"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""
word = 'natan'
lista = list(word)

lista.reverse()

if lista == list(word):
    print("Palindromo")
else:
    print("No Palindromo")

# word = 'natan'

# if word[::-1] == word:
#     print("Palindromo")
# else:
#     print("No es Palindromo")