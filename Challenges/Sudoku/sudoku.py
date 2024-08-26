def eh_valido(sudoku, linha, coluna, numero):
    # Verifica se o número já existe na linha
    if numero in sudoku[linha]:
        return False

    # Verifica se o número já existe na coluna
    if numero in [sudoku[i][coluna] for i in range(9)]:
        return False

    # Verifica se o número já existe na subgrade 3x3
    subgrade_linha = (linha // 3) * 3
    subgrade_coluna = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[subgrade_linha + i][subgrade_coluna + j] == numero:
                return False

    return True

def resolver_sudoku(sudoku):
    for linha in range(9):
        for coluna in range(9):
            if sudoku[linha][coluna] == 0:  # Encontra uma célula vazia
                for numero in range(1, 10):  # Tenta números de 1 a 9
                    if eh_valido(sudoku, linha, coluna, numero):
                        sudoku[linha][coluna] = numero
                        if resolver_sudoku(sudoku):
                            return sudoku
                        sudoku[linha][coluna] = 0  # Backtrack
                return False  # Se nenhum número funcionar, volta atrás
    return True

def mostrar_sudoku(sudoku):
    print("-" * 57)
    for i, linha in enumerate(sudoku):
        print(" | ".join(" ".join(str(linha[j:j + 3])) for j in range(0, 9, 3)))
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 57)
    print("-" * 57)

# Sudoku de exemplo
sudoku_exemplo = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Resolver e exibir o Sudoku
if resolver_sudoku(sudoku_exemplo):
    mostrar_sudoku(sudoku_exemplo)
else:
    print("Não foi possível resolver o Sudoku.")
