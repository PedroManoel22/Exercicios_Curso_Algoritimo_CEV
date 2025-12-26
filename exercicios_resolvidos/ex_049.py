# 49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles 
# são pares e quantos são ímpares. 

from ex_048 import ler_nums_int

def e_par(nums):
    nums_pares = []

    for num in nums:
        if num % 2 == 0:
            nums_pares.append(num)
    
    qtd = len(nums_pares)
    return nums_pares, qtd


def e_impar(nums):
    nums_impares = []

    for num in nums:
        if num % 2 != 0:
            nums_impares.append(num)
    qtd = len(nums_impares)
    return nums_impares, qtd


def mostrar_dados(nums, pares,qtd_pares, impares, qtd_impares):
    print(f'\nNúmeros digitados: {nums}\n'
          f'Pares: {pares}, quantidade = {qtd_pares}\n'
          f'Ímpares: {impares}, quantidade = {qtd_impares}\n')



if __name__ == '__main__':
    nums = ler_nums_int(6)
    pares = e_par(nums)
    impares = e_impar(nums)
    mostrar_dados(nums, *pares, *impares)
