import features as game
import random
import featuresMODO2 as game2

while True:
    a2 = 1
    b2 = 20
    print(f"\nBem-vindo ao Tigrinho 2!\nSeu objetivo é adivinhar o número secreto!\n\nMODOS DE JOGO:\n1. Quente ou Frio\n\tVocê terá algumas tentativas de acertar o número, quando lançar um palpite saberá se está próximo ou não!\n2. Dicas\n\tVocê terá 4 chances de adivinhar um número, a cada palpite será dada uma dica nova!\n3. Sair do jogo\n")
    modo = int(input("Escolha o modo de jogo: "))
    if modo == 1:
        while True:
            print(f"Níveis de dificuldade:\n\n1. Bebê (16 vidas e 16 números)\n2. Fácil (8 vidas e 16 números)\n3. Normal (4 vidas e 20 números)\n4. Difícil (3 vidas e 30 números)\n5. Impossível (5 vidas e 100 números)\n6. Voltar para o menu principal\n")
            dificuldade = int(input("Escolha a dificuldade: "))
            if  dificuldade == 1:
                a1= 1
                b1 = 16
                vidas_modo1 = 16
                break
            elif dificuldade == 2:
                a1 = 1
                b1 = 16
                vidas_modo1 = 8
                break
            elif dificuldade == 3:
                a1 = 1
                b1 = 20
                vidas_modo1 = 4
                break
            elif dificuldade == 4:
                a1 = 1
                b1 = 30
                vidas_modo1 = 3
                break
            elif dificuldade == 5:
                a1 = 1
                b1 = 100
                vidas_modo1 = 5
                break
            elif dificuldade == 6:
                break
            else:
                print("\n===Comando inválido, tente digitar um número de 1 a 6!===")

        if dificuldade != 6:
            m = random.randint(a1 , b1)
            while vidas_modo1 > 0:
                game.modo1(m , vidas_modo1 , a1 , b1)
                vidas_modo1 = vidas_modo1 - 1
            game.derrota(m)

    elif modo == 2:
        
        m = random.randint(a2 , b2)
        if game2.modo2(a2 , b2 , m):
            game.vitoria(m)
        else:
            game.derrota(m)

    elif modo == 3:
        print("\n===Você saiu!===")
        exit()
    else:
        print("\n===Comando inválido, tente digitar um número de 1 a 3!===")