import pandas as pd

# POSICIÓN GLOBAL
global line, col, stack_col

def reset_globals():
    """Reinicia las variables globales antes de cada análisis."""
    global line, col, stack_col
    line = 1
    col = 0
    stack_col = []

def lexical_analysis(code):
    global line, col

    # Reinicia las variables globales al inicio del análisis
    reset_globals()

    # Lee la matriz desde un archivo Excel
    matrix = pd.read_excel('./myproject/matriz.xlsx')
    spaces = [' ', '\t', '\n']
    pila_comillas = []
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "_", "<", ">", "=", "!", "&", "|", "+", "-", "*", "/", "(", ")", "{", "}",
        "[", "]", "\"", ".", " ", "jmp", "tab", ";"
    ]

    result = []
    token = ""
    token_start_col = 1  # Para rastrear la columna donde empieza el token
    row = 0  # Estado inicial = 0

    for char in code:
        column = procesar_char(char)
        if column not in alphabet:
            col_pos = token_start_col
            result.append([token, "ERROR", line, col_pos])
            break

        if isinstance(matrix[column][row], int):
            row = matrix[column][row]
            if char == "\"":
                if not pila_comillas:
                    pila_comillas.append(char)
                else:
                    pila_comillas.pop()
            else:
                if char not in spaces:
                    if not token:
                        token_start_col = col  # Marca el inicio del token
                    token += char
                elif pila_comillas:
                    token += char
        else:
            col_pos = token_start_col
            result.append([token, matrix[column][row], line, col_pos])
            if matrix[column][row] == "er" or matrix[column][row] == "e":
                result.append([token, matrix[column][row], line, col_pos])
                break
            token = ""
            row = 0
            if char not in spaces:
                token_start_col = col  # Actualiza la posición inicial del nuevo token
                token += char
                row = matrix[column][row]
                if not isinstance(matrix[column][row], int) and str(matrix[column][row]) != "er":
                    col_pos = token_start_col
                    result.append([token, matrix[column][row], line, col_pos])
                    token = ""
                    row = 0

    return result

def procesar_char(char):
    global line, col
    col += 1
    if char.isdigit():
        column = int(char)
    else:
        column = str(char)

    if char == "\n":
        column = "jmp"
        stack_col.append(col)
        line += 1
        col = 0  # Reinicia la columna en una nueva línea
    elif char == "\t":
        column = "tab"
        col += 3  # Avanza la columna en 4 espacios
    return column
