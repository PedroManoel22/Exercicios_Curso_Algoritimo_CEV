# 31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura) 

def Jogada_usuario():
    jogadas_possiveis = ['1', '2', '3']
    jogada_nomes = ['Pedra', 'Papel', 'Tesoura']

    while True:
        jogada = input('Insira sua opção: ')
        if jogada in jogadas_possiveis:
            break

        else:
            print('\n\033[1;31mPor favor coloque um opção válida!\033[m\n')
    
    posicao = int(jogada) - 1
    jogada = jogada_nomes[posicao]
    
    return jogada

def cabecalho():
    print('\n---- JoKenPo ----\n')
    print('[1] Pedra\n'
          '[2] Papel\n'
          '[3] Tesoura\n')


def jogada_computador():
    from random import randint

    jogada_nomes = ['Pedra', 'Papel', 'Tesoura']

    jogada = randint(1,3)
    posicao = jogada - 1
    jogada = jogada_nomes[posicao]
    
    return jogada


def resultado(jogada_usuario, jogada_computador):
    
    
    if jogada_usuario == jogada_computador:
        return 'DEU EMPATE!'
    
    elif jogada_usuario == 'Pedra' and jogada_computador == 'Tesoura':
        return True

    elif jogada_usuario == 'Papel' and jogada_computador == 'Pedra':
        return True

    elif jogada_usuario == 'Tesoura' and jogada_computador == 'Papel':
        return True

    
    return False


def exibir_dados(j_usuario, j_computador):
    print(f'\nSua jogada: {j_usuario}\n'
          f'Jogada do computador: {j_computador}\n\n'
          '---- Resultado ----')
    

if __name__ == '__main__':
    while True:
        cabecalho()
        j_usuario = Jogada_usuario()
        j_computador = jogada_computador()
        ganhou = resultado(j_usuario, j_computador)
        exibir_dados(j_usuario, j_computador)
        if ganhou == 'DEU EMPATE!':
            print('\n\033[1;33mDEU EMPATE!\033[m\n')

        elif ganhou:
            print('\n\033[1;32mParabéns, você ganhou!\033[m\n')
        
        else:
            print('\n\033[1;31mVocê perdeu!\033[m\n')
        
        opcao = input('Deseja Continuar? [S/N]: ').strip().upper()

        if opcao == 'N':
            break

        elif opcao == 'S':
            continue

        print('\nComo você não colocou nem sim e nem não vou considerar como um sim\n')

      