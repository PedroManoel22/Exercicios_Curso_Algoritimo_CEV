# 48) Faça um programa que leia 7 números inteiros e no final mostre o somatório 
# entre eles. 

from ex_046 import somar

def ler_nums_int(qtd):
    nums = []
    for i in range(1, qtd + 1):
        while True:
            try:
                num = int(input(f'Insira o {i}° número: '))
                nums.append(num)
                break
            
            except ValueError:
                print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')

    return nums


def mostrar_dados(nums, soma):
    print('\nA soma entre ', end='')
    for num in nums:
        print(f'{num}, ', end='')
    
    print(f'\nÉ igual a {soma}')

if __name__ == '__main__':
    nums = ler_nums_int(7)
    soma = somar(nums)
    mostrar_dados(nums, soma)


