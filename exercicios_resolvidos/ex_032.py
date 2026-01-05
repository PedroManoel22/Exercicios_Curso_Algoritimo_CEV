# 32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o 
# jogador vai tentar descobrir qual foi o valor sorteado.

def sortea_um_a_cinco():
    from random import randint

    num = randint(1,5)

    return num 


def advinhacao_usuario(qtd):
    from time import sleep
    numeros = [x for x in range(1, qtd + 1)]
    primeiro_num = numeros[0]
    ultimo_num = numeros[-1]

    print(f'\nEstou pensando em um número de {primeiro_num} a {ultimo_num} .....\n')
    sleep(2)

    while True:
        try:
            resposta = int(input('Tente adivinhar o número que pensei: '))
            if resposta not in numeros:
                print(f'\n\033[1;33mPor favor coloque um número inteiro entre {primeiro_num} e {ultimo_num}!\033[m\n')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
    
    return resposta


def resultado(num_computador, num_usuario):
    if num_computador == num_usuario:
        return True
        
    else:
        return False
        

    

if __name__ == '__main__':
    num_computador = sortea_um_a_cinco()
    num_usuario = advinhacao_usuario(5)
    r = resultado(num_computador, num_usuario)
    if r:
        resposta = '\033[1;32mAcertou!\033[m'
    
    else:
        resposta = '\033[1;31mErrou!\033[m'

    print(f'\nNúmero que pensei: {num_computador}\n'
          f'Número que você me mandou: {num_usuario}\n'
          f'Resposta: {resposta}\n')

