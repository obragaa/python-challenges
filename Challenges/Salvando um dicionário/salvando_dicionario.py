import pickle

def salvar_dicio(dicionario, caminho_arquivo):
    with open(caminho_arquivo, 'wb') as arquivo:  # 'wb' para escrita em modo binário
        pickle.dump(dicionario, arquivo)

def carregar_dicio(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as arquivo:  # 'rb' para leitura em modo binário
        return pickle.load(arquivo)

# Criando um dicionário de teste
dicio_teste = {1: 'a', 2: 'b', 3: 'c'}

# Salvando o dicionário
salvar_dicio(dicio_teste, 'dicio.pickle')

# Carregando o dicionário
dicio_carregado = carregar_dicio('dicio.pickle')

# Verificando se o dicionário foi carregado corretamente
print(dicio_carregado)  # Saída esperada: {1: 'a', 2: 'b', 3: 'c'}
