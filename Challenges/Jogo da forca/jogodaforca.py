import os
import random

# Função para escolher o tema e a palavra
def escolher_palavra():
    temas = {
        'Animais': ['elefante', 'girafa', 'cachorro', 'gato'],
        'Frutas': ['banana', 'morango', 'abacaxi', 'laranja'],
        'Cores': ['vermelho', 'azul', 'verde', 'amarelo'],
        'Países': ['brasil', 'argentina', 'portugal', 'alemanha']
    }
    
    tema_escolhido = random.choice(list(temas.keys()))
    palavra_escolhida = random.choice(temas[tema_escolhido])
    
    return tema_escolhido, palavra_escolhida

# Função para exibir o estado atual do jogo
def mostrar_jogo(tema, palavra, tentativas_restantes, chutes):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Tema: {tema}")
    print("Palavra: ", ' '.join([letra if letra in chutes else '_' for letra in palavra]))
    print(f"Tentativas restantes: {tentativas_restantes}")
    print(f"Letras já chutadas: {' '.join(sorted(chutes))}")

# Função principal do jogo da forca
def jogo_da_forca():
    tema, palavra = escolher_palavra()
    tentativas_restantes = len(palavra) - 1
    chutes = set()
    
    while tentativas_restantes > 0:
        mostrar_jogo(tema, palavra, tentativas_restantes, chutes)
        chute = input("Digite uma letra: ").lower()
        
        if chute in chutes:
            print("Você já chutou essa letra. Tente outra.")
            continue
        
        chutes.add(chute)
        
        if chute in palavra:
            if all(letra in chutes for letra in palavra):
                mostrar_jogo(tema, palavra, tentativas_restantes, chutes)
                print("Parabéns! Você acertou a palavra!")
                break
        else:
            tentativas_restantes -= 1
            if tentativas_restantes == 0:
                mostrar_jogo(tema, palavra, tentativas_restantes, chutes)
                print(f"Game Over! A palavra era '{palavra}'.")
                break

# Iniciar o jogo
jogo_da_forca()
