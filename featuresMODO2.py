"""" FUNÇÕES DO JOGO DOS NÚMEROS """

def primo(n):
    divisores = 0
    for i in range(n):
        if n / (i + 1) % 1 == 0:
            divisores += 1
    
    if divisores == 2:
        print("===Dica: O número secreto é primo!===")
    else:
        print("===Dica: O número secreto não é primo!===")

# Fazer funções de fib, quadrado, curiosidades e o outro modo
    
def fib(n):
    fib = [1 , 2 , 3 , 5 , 8 , 13]
    if n in fib:
        print("===Dica: O número secreto é um número de Fibonacci!===")
    else:
        print("===Dica: O número secreto não é um número de Fibonacci!===")
    
def pedirnumero(a , b , vidas):
    return int(input(f"\nVocê tem {vidas} vida(s)!\n\nDê um palpite de um número de {a} a {b}: "))
    
curiosidades = {1:"Número de estatuetas do Oscar do Leonardo DiCaprio" , 
                2:"Fortuna do Edir Macedo em bilhões de doláres" ,
                3:"Primeiro número primo de Fermat" ,
                4:"Número de títulos do Brasileirão do Vasco da Gama" ,
                5:"Número Atômico do Boro" ,
                6:"Comprimento médio de um elefante asiático" ,
                7:"Quantidade de anos que a Etiopia está atrasada no calendário em relação ao ocidente" ,
                8:"Tempo em minutos aproximado para a luz do Sol chegar na Terra" ,
                9:"Nome do filme do Ryan Reynolds" ,
                10:"Percentual do território russo em relação à superfície terrestre" ,
                11:"Número de albuns de estúdio da Taylor Swift" ,
                12:"Quantidade de olhos de uma borboleta (em milhares de olhos)" ,
                13:"Recorde em segundos de voo de uma galinha" ,
                14:"Quantidade de países da Oceania" ,
                15:"Século de invenção do Cachorro Quente" ,
                16:"Número eleitoral do Partido Socialista dos Trabalhadores Unificado" ,
                17:"Número do primeiro episódio de Pokemon onde os pokemons falam" ,
                18:"Jyuhati" ,
                19:"Século de criação do braile" ,
                20:"Quantidade de mortos na primeira guerra mundial (em milhões)"}
    
def modo2(a , b , m):
    n = pedirnumero(a , b , 4)
    if n == m:
        return True
    else:
        primo(m)

    n = pedirnumero(a , b , 3)
    if n == m:
        return True
    else:
        fib(m)

    n = pedirnumero(a , b , 2)
    if n == m:
        return True
    else:
        print("Dica:" , curiosidades[m])

    n = pedirnumero(a , b , 1)
    if n == m:
        return True
    else:
        return False

