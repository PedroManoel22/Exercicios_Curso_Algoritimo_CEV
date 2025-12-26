# 50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e 
# mostre na tela: 
# a) Quais foram os números sorteados 
# b) Quantos números estão acima de 5 
# c) Quantos números são divisíveis por 3

def sorteia_numeros(qtd_numeros, inicio, fim):
    from random import randint
    from time import sleep
    nums = []

    print(f'\n\033[1;32mEstou sorteando {qtd_numeros} números entre {inicio} e {fim}....\033[m')
    sleep(3)

    for _ in range(qtd_numeros):
        nums.append(randint(inicio, fim))
    
    return nums


def qtd_nums_acima_5(nums):
    qtd = 0
    for num in nums:
        if num > 5:
            qtd += 1
    
    return qtd


def qtd_nums_divisiveis_3(nums):
    qtd = 0
    for num in nums:
        if num % 3 == 0:
            qtd += 1
    
    return qtd


def exibir_dados(nums, acima_cinco, divisiveis_tres):
    print(f'\nNúmeros sorteados: {nums}\n\n'
          f'Quantidade de números maiores que 5: {acima_cinco}\n\n'
          f'Quantidade de números divisíveis por 3: {divisiveis_tres}\n')

if __name__ == '__main__':
    QTD_NUMS = 20
    INICIO = 0
    FIM = 10

    nums_sorteados = sorteia_numeros(QTD_NUMS, INICIO, FIM)
    nums_acima_cinco = qtd_nums_acima_5(nums_sorteados)
    nums_divisiveis_3 = qtd_nums_divisiveis_3(nums_sorteados)
    exibir_dados(nums_sorteados, nums_acima_cinco, nums_divisiveis_3)
    
