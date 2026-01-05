# 56) Crie um programa que leia vários números pelo teclado e mostre no final o 
# somatório entre eles. 
# Obs: O programa será interrompido quando o número 1111 for digitado 

def ler_numeros():
    nums = []
    while True:
        try:
            num = int(input('\nDigite um número: [1111] para cancelar: '))
            if num != 1111:
                nums.append(num)
            if num == 1111:
                break

        except ValueError:
            print('\033[1;31m\nPor favor insira um número inteiro!\033[m')
            continue

    
    return nums


def somatorio(nums):
    soma = 0
    for num in nums:
        soma += num
    
    return soma


def exibir_dados(nums, soma):
    print(f'\nNúmeros: {nums}\n'
          f'Somatório: {soma}\n')


if __name__ == '__main__':
    numeros = ler_numeros()
    soma = somatorio(numeros)
    exibir_dados(numeros, soma)