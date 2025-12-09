# 32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o 
# jogador vai tentar descobrir qual foi o valor sorteado.

def sortea_um_a_cinco():
    from random import randint

    num = randint(1,5)

    return num 


def advinhacao_usuario():
    from time import sleep
    numeros = [x for x in range(1, 6)]

    print('\nEstou pensando em um número de 1 a 5 .....\n')
    sleep(2)

    while True:
        try:
            resposta = int(input('Tente adivinhar o número que pensei: '))
            if resposta not in numeros:
                print('\n\033[1;33mPor favor coloque um número inteiro entre 1 e 5!\033[m\n')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
    
    return resposta


def resultado(num_computador, num_usuario):
    if num_computador == num_usuario:
        resposta = '\033[1;32mAcertou!\033[m'
        
    else:
        resposta = '\033[1;31mErrou!\033[m'

    print(f'\nNúmero que pensei: {num_computador}\n'
          f'Número que você me mandou: {num_usuario}\n'
          f'Resposta: {resposta}\n')


if __name__ == '__main__':
    num_computador = sortea_um_a_cinco()
    num_usuario = advinhacao_usuario()
    resultado(num_computador, num_usuario)
