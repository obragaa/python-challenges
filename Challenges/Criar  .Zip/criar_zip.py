import os
import zipfile

def compactar(diretorio, extensoes, arquivo_saida):
    # Cria o arquivo ZIP
    with zipfile.ZipFile(arquivo_saida, 'w') as arquivo_zip:
        # Percorre o diretório e os subdiretórios
        for raiz, _, arquivos in os.walk(diretorio):
            # Cria um caminho relativo para manter a estrutura de pastas
            caminho_relativo = os.path.relpath(raiz, diretorio)
            
            for arquivo in arquivos:
                # Separa o nome do arquivo e a extensão
                _, extensao = os.path.splitext(arquivo)
                
                # Verifica se a extensão está na lista de extensões de interesse
                if extensao.lower() in extensoes:
                    caminho_absoluto = os.path.join(raiz, arquivo)
                    # Adiciona o arquivo ao ZIP, mantendo a estrutura de diretórios
                    arquivo_zip.write(caminho_absoluto, os.path.join(caminho_relativo, arquivo))

# Exemplo de uso
diretorio = 'para_compactar'
extensoes = ['.jpg', '.txt']
arquivo_saida = 'minhas_fotos.zip'

compactar(diretorio, extensoes, arquivo_saida)
