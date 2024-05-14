import features as game
import random

while True:
    a = 1
    b = 20
    vidas = 4
    print(f"\nBem-vindo ao Tigrinho 2!\nSeu objetivo é adivinhar o número secreto!\n\nMODOS DE JOGO:\n1. Quente ou Frio\n\tVocê terá {vidas} tentativas de acertar o número, quando lançar um palpite saberá se está próximo ou não!\n2. Dicas (Em breve!)\n3. Sair do jogo\n")
    modo = int(input("Escolha o modo de jogo: "))
    if modo == 1:
        
        m = random.randint(a , b)
        while vidas > 0:
            game.modo1(m , vidas , a , b)
            vidas = vidas - 1
        game.derrota(m)

    elif modo == 2:
        print("\n===Modo de jogo ainda não disponível!===")
    elif modo == 3:
        print("\n===Você saiu!===")
        exit()
    else:
        print("\n===Comando inválido, tente digitar um número de 1 a 3!===")