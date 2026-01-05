# 55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de 
# agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 
# tentativas para tentar acertar.

from ex_032 import advinhacao_usuario, resultado
def sortea_um_a_dez():
    from random import randint

    num = randint(1,10)

    return num 

if __name__ == '__main__':
    num_computador = sortea_um_a_dez()
    
    for i in range(1, 5):
        print(f'\ntentavida {i} de 4\n')
        num_usuario = advinhacao_usuario(10)
        r = resultado(num_computador, num_usuario)
        if r:
            resposta = '\033[1;32mParabéns você acertou!\033[m\n'
            break
        else:
            print('\n\033[1;31mTente novamente!\033[m')
            resposta = '\033[1;31mVocê perdeu!\033[m\n'
    
    print(f'\nNúmero que pensei: {num_computador}\n'
          f'Número que você me mandou: {num_usuario}\n'
          f'Resposta: {resposta}')

