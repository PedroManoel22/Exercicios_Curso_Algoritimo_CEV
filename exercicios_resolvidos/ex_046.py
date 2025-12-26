# 46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 
# 8 + 10 + 12 + 14 + ... + 98 + 100. 


def somar(nums):
    soma = sum(nums)
    return soma


def mostrar_dados(nums, soma):
    print(f'\nA soma entre {nums[0]} + {nums[1]} + {nums[2]} + {nums[3]} + {nums[4]} + .... + {nums[-2]} + {nums[-1]}.\n')
    print(f'É igual a {soma}\n')


if __name__ == '__main__':
    INTERVALO = [x for x in range(6, 101) if x % 2 == 0]
    soma = somar(INTERVALO)
    mostrar_dados(INTERVALO, soma)
