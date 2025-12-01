# 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu 
# PREÇO PROMOCIONAL, com 5% de desconto. 

def valida_preco():
    while True:
        try:
            preco = float(input('Digite o preço do produto: '))
            if preco <= 0:
                print('\n\033[1;31mO preço do produto não pode ser igual a 0 ou menor\033[m\n')

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número válido!\n\033[m')
    
    return preco


def calcula_desconto(preco):
    desconto = 0.05
    preco_com_desconto = preco - (preco * desconto)
    return preco_com_desconto


def mostra_dados(preco, preco_com_desconto):
    print(f'Preço normal: R${preco}\n'
          f'Preço com desconto: R${preco_com_desconto}')


if __name__ == '__main__':
    preco = valida_preco()
    desconto = calcula_desconto(preco)
    mostra_dados(preco, desconto)
