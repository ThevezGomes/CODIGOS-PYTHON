def modulo(n):
    if n < 0:
        mod = n * (-1)
    else:
        mod = n
    
    return mod

def quentefrio(m, n , a , b):
    dif = modulo(m - n)
    ran = modulo(b - a) + 1
    if dif > 0 and dif <= (ran // 16):
        print("Pelando!")
    elif dif > (ran // 16) and dif <= (ran // 8):
        print("Quente!")
    elif dif > (ran // 8) and dif <= (ran // 4):
        print("Morno!")
    elif dif > (ran // 4) and dif <= (ran // 2):
        print("Frio!")
    elif dif == 0:
        return True
    else:
        print("Congelando...")

def vitoria(m):
    print("Você acertou!\nO número secreto era" , m)
    exit()

def derrota(m):
    print("Você perdeu! Suas vidas acabaram! O número secreto era" , m)
    exit()

def modo1(m , vidas , a , b):
    n = int(input(f"\nVocê tem {vidas} vidas!\n\nDê um palpite de um número de {a} a {b}: "))
    if quentefrio(m , n , a , b):
        vitoria(m)
    



