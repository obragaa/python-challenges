import secrets

def gerar_senha(numero_de_palavras, caminho_diceware='wordlist_en_eff.txt'):
    # Abrir e ler o arquivo de palavras Diceware
    with open(caminho_diceware, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    # Filtrar apenas as palavras, ignorando os números associados
    palavras = [linha.split()[1] for linha in linhas[3:7779]]  # Índices baseados no exemplo dado

    # Escolher palavras aleatórias
    senha = ' '.join(secrets.choice(palavras) for _ in range(numero_de_palavras))
    
    return senha

# Exemplo de uso
print(gerar_senha(7))  # Gera uma senha com 7 palavras
