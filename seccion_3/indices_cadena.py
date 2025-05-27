
bidimensional = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

# Acceder a un carácter específico en una cadena bidimensional
caracter_bi = bidimensional[1][2].upper()  # Convertir a mayúscula

for fila in bidimensional:
    for elemento in fila:
        print(elemento, end=" ")
    print()
  