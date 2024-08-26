def ordenando_palavras(s):
    # Divide a string em palavras
    palavras = s.split()

    # Ordena as palavras ignorando a capitalização
    palavras_ordenadas = sorted(palavras, key=str.casefold)

    # Junta as palavras ordenadas de volta em uma string
    return ' '.join(palavras_ordenadas)

# Testando a função
print(ordenando_palavras("maçã LARANJA banana"))  # Saída: "banana LARANJA maçã"
print(ordenando_palavras("Casa arvore ZEBRA relogio"))  # Saída: "árvore Casa relógio ZEBRA"
