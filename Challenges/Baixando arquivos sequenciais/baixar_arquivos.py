import os
import re
import urllib.request
import urllib.parse

def baixar_arquivos(url_inicial, diretorio_saida):
    # Verifica se o diretório de saída existe, se não, cria
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    
    # Separa a URL nas suas partes componentes
    url_parts = list(urllib.parse.urlsplit(url_inicial))
    
    # Identifica o número na URL
    padrao = re.compile(r'(\d+)')
    match = padrao.search(url_parts[2])
    
    if not match:
        print("Não foi possível encontrar um número na URL.")
        return
    
    num_inicial = match.group(0)
    indice_atual = int(num_inicial)
    contador_erro = 0
    
    while contador_erro < 3:
        # Gera o novo número da sequência, mantendo o formato (zeros à esquerda)
        novo_numero = str(indice_atual).zfill(len(num_inicial))
        
        # Substitui o número antigo pelo novo na URL
        url_parts[2] = padrao.sub(novo_numero, url_parts[2], 1)
        url_nova = urllib.parse.urlunsplit(url_parts)
        
        # Define o nome do arquivo e o caminho de salvamento
        nome_arquivo = os.path.basename(url_parts[2])
        caminho_arquivo = os.path.join(diretorio_saida, nome_arquivo)
        
        try:
            print(f"Baixando {url_nova} ...")
            urllib.request.urlretrieve(url_nova, caminho_arquivo)
            print(f"Arquivo salvo em: {caminho_arquivo}")
            contador_erro = 0  # Reseta o contador de erros após um download bem-sucedido
        except Exception as e:
            print(f"Erro ao baixar {url_nova}: {e}")
            contador_erro += 1
        
        indice_atual += 1

# Exemplo de uso
url_inicial = "https://imgs.search.brave.com/QlI3VhMNt8Zz9vPnBVV5FeBBvMC6Af5jOgRFEfz3_jw/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9sb2dv/cy1kb3dubG9hZC5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MTYvMTAvUHl0aG9u/X2xvZ29faWNvbi03/MDB4Njk3LnBuZw"  # Substitua por uma URL válida
diretorio_saida = "imagens_baixadas"

baixar_arquivos(url_inicial, diretorio_saida)
