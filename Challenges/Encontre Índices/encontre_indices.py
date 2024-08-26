def encontre_indices(lista, valor):
    indices_encontrados = []

    def buscar(lista, valor, caminho_atual):
        for i, item in enumerate(lista):
            novo_caminho = caminho_atual + [i]
            if item == valor:
                indices_encontrados.append(novo_caminho)
            elif isinstance(item, list):
                buscar(item, valor, novo_caminho)

    buscar(lista, valor, [])
    return indices_encontrados

# Testando a função com o exemplo fornecido
lista_exemplo = [
    [[1, 2, 3], [4, 2, 5]],
    [[6, 7, 8], [2, 9]]
]

print(encontre_indices(lista_exemplo, 2))
# Saída esperada: [[0, 0, 1], [0, 1, 1], [1, 1, 0]]
