import re
import collections

def contar_palavras(caminho_arquivo):
    # Ler o conteúdo do arquivo
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
    
    # Extrair as palavras usando regex
    palavras = re.findall(r"\b[\w'-]+\b", conteudo.lower())
    
    # Contar a frequência de cada palavra
    contador_palavras = collections.Counter(palavras)
    
    # Número total de palavras
    total_palavras = len(palavras)
    print(f"Total de palavras: {total_palavras}")
    
    # As 20 palavras mais comuns
    palavras_mais_comuns = contador_palavras.most_common(20)
    print("\nAs 20 palavras mais comuns:")
    for palavra, contagem in palavras_mais_comuns:
        print(f"{palavra}: {contagem}")

# Exemplo de uso
contar_palavras('seu_arquivo.txt')
