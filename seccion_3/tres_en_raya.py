import random

# Tablero vacío
tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    for i, fila in enumerate(tablero):
        print(" | ".join(fila))
        if i < 2:
            print("--+---+--")

# Colocar una ficha
def jugar_turno(tablero, fila, columna, simbolo):
    if 0 <= fila < 3 and 0 <= columna < 3:
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = simbolo
            return True
        else:
            print("Esa posición ya está ocupada. Intenta de nuevo.")
    else:
        print("Fila o columna fuera de rango (0-2).")
    return False

# Verificar si hay un ganador
def verificar_ganador(tablero, simbolo):
    # Filas y columnas
    for i in range(3):
        if all(tablero[i][j] == simbolo for j in range(3)) or all(tablero[j][i] == simbolo for j in range(3)):
            return True
    # Diagonales
    if all(tablero[i][i] == simbolo for i in range(3)) or all(tablero[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

# Verificar si el tablero está lleno
def tablero_lleno(tablero):
    return all(celda != ' ' for fila in tablero for celda in fila)

# Turno de la IA
def turno_ia(tablero):
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = 'O'
            print(f"\nIA ha jugado en ({fila}, {columna})")
            break

# Bucle principal del juego
while True:
    mostrar_tablero(tablero)

    # Turno del jugador
    while True:
        try:
            fila = int(input("Jugador 1, ingresa la fila (0-2): "))
            columna = int(input("Jugador 1, ingresa la columna (0-2): "))
            if jugar_turno(tablero, fila, columna, 'X'):
                break
        except ValueError:
            print("Entrada inválida. Usa solo números del 0 al 2.")

    if verificar_ganador(tablero, 'X'):
        mostrar_tablero(tablero)
        print("¡Jugador 1 gana!")
        break
    if tablero_lleno(tablero):
        mostrar_tablero(tablero)
        print("¡Empate!")
        break

    # Turno IA
    turno_ia(tablero)

    if verificar_ganador(tablero, 'O'):
        mostrar_tablero(tablero)
        print("¡La IA gana!")
        break
    if tablero_lleno(tablero):
        mostrar_tablero(tablero)
        print("¡Empate!")
        break
