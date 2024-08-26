import time
import random

def jogo_de_espera():
    # Gera um tempo aleatório entre 2 e 4 segundos
    tempo_espera = random.randint(2, 4)
    
    print(f"Tente esperar por {tempo_espera} segundos.")
    input("Pressione ENTER para começar...")
    
    # Inicia o cronômetro
    inicio = time.time()
    input("Pressione ENTER novamente após o tempo estimado...")
    
    # Calcula o tempo decorrido
    fim = time.time()
    tempo_decorrido = fim - inicio
    
    print(f"Você esperou por {tempo_decorrido:.3f} segundos.")
    
    # Verifica se o tempo foi dentro da margem de acerto
    if tempo_decorrido < tempo_espera:
        print("Muito rápido!")
    elif tempo_decorrido > tempo_espera:
        print("Muito lento!")
    else:
        print("Você acertou em cheio!")

# Executando o jogo
jogo_de_espera()
