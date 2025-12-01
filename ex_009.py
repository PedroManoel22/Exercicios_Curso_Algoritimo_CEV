# 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) 
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45. 

def valida_dinheiro():
    while True:
        try:
            dinheiro = float(input('Quanto reias você tem na carteira:  '))
            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número real!\n\033[m')
    
    return dinheiro


def converte_dinheiro(dinheiro_reais):
    dinheiro_us = round(dinheiro_reais / 3.45, 2)
    print(f'Você pode comprar US${dinheiro_us}')


if __name__ == '__main__':
    dinheiro = valida_dinheiro()
    converte_dinheiro(dinheiro)
