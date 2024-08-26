import csv

def unir_csv(caminhos_arquivos, caminho_saida):
    # Passo 1: Identificar todos os cabeçalhos únicos
    todos_campos = set()
    
    for caminho in caminhos_arquivos:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            todos_campos.update(leitor.fieldnames)
    
    todos_campos = sorted(todos_campos)  # Ordena os campos para uma ordem consistente
    
    # Passo 2: Escrever os dados no arquivo de saída
    with open(caminho_saida, 'w', newline='', encoding='utf-8') as arquivo_saida:
        escritor = csv.DictWriter(arquivo_saida, fieldnames=todos_campos)
        escritor.writeheader()
        
        for caminho in caminhos_arquivos:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    escritor.writerow(linha)

# Exemplo de uso
caminhos_arquivos = ['turma1.csv', 'turma2.csv']
caminho_saida = 'alunos.csv'
unir_csv(caminhos_arquivos, caminho_saida)
