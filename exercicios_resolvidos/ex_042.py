# 42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo 
# qualquer e mostre uma contagem até esse valor: 
# Ex: Digite um valor: 35 
# Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou! 

from ex_006 import valida_num_int

num_int = valida_num_int()

def mostrar_contagem(num):
    nums = [x for x in range(1, num + 1)]

    print()
    for n in nums:
        print(f'{n} ', end='')
    
    print('Acabou!\n')

mostrar_contagem(num_int)
