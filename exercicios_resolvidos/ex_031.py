# 31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura) 

def Jogada_usuario():
    jogadas_possiveis = ['1', '2', '3']
    while True:
        jogada = input('Insira sua opção: ')
        if jogada in jogadas_possiveis:
            break
        else:
            print('\n\033[1;31mPor favor coloque um opção válida!\033[m\n')
    

def cabecalho():
    print('\n---- JoKenPo ----\n')
    print('[1] Pedra\n'
          '[2] Papel\n'
          '[3] Tesoura\n')
