# 52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final: 
# a) Qual é a média de idade do grupo 
# b) Quantas pessoas tem mais de 18 anos 
# c) Quantas pessoas tem menos de 5 anos 
# d) Qual foi a maior idade lida

def ler_idades(qtd):
    idades = []
    for i in range(1, qtd + 1):
        while True:
            try:
                idade = int(input(f'Insira a idade da {i}° pessoa: '))
                idades.append(idade)
                break
            
            except ValueError:
                print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')

    return idades


def calcula_media(idades):
    import numpy as np
    media = np.mean(idades)
    return media


def calcula_qtd_maiores_18(idades):
    maiores = []

    for n in idades:
        if n > 18:
            maiores.append(n)

    maiores = len(maiores)

    return maiores


def calcula_qtd_menores_5(idades):
    menores = []

    for n in idades:
        if n < 18:
            menores.append(n)
    
    menores = len(menores)
            
    return menores


def exibir_dados(idades, media, maiores, menores):
    print(f'\nIdades inseridas: {idades}\n'
          f'Idade média: {media:.2f} anos\n'
          f'Quantidade de maiores de 18 anos: {maiores} \n'
          f'Quantidade de menores de 5 anos: {menores}\n')


if __name__ == '__main__':
    idades = ler_idades(10)
    media = calcula_media(idades)
    qtd_maiores = calcula_qtd_maiores_18(idades)
    qtd_menores = calcula_qtd_menores_5(idades)
    exibir_dados(idades, media, qtd_maiores, qtd_menores)
