import random
import collections

def simular_dados(*dados, num_simulacoes=1000000):
    # Inicializa o contador para armazenar os resultados
    resultados = collections.Counter()
    
    # Simula os lançamentos
    for _ in range(num_simulacoes):
        soma = sum(random.randint(1, lados) for lados in dados)
        resultados[soma] += 1
    
    # Calcula e imprime as probabilidades
    print("Resultado | Probabilidade")
    print("--------------------------")
    for resultado in range(min(dados), sum(dados) + 1):
        probabilidade = resultados[resultado] / num_simulacoes * 100
        print(f"{resultado:^8} | {probabilidade:.2f}%")

# Exemplo de uso:
# Dado de 4 lados e dois dados de 6 lados
simular_dados(4, 6, 6)
