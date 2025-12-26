# 51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela 
# qual foi o maior e qual foi o menor preço digitados. 

def ler_precos(qtd):
    precos = []
    for i in range(1, qtd + 1):
        while True:
            try:
                num = float(input(f'Insira o preço do {i}° produto: '))
                precos.append(num)
                break
            
            except ValueError:
                print('\n\033[1;31mPor favor coloque um valor válido!\033[m\n')

    return precos


def menor_preco(precos):
    menor = min(precos)
    return menor

def exibir_dados(menor):
    print(f'\nMenor preço: R${menor:.2f}')


if __name__ == '__main__':
    QTD_PRODUTOS = 8
    precos = ler_precos(QTD_PRODUTOS)
    menor = menor_preco(precos)
    exibir_dados(menor)
