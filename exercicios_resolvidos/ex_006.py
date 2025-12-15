# 6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu 
# sucessor. 
# Ex:  
# Digite um número: 9 
# O antecessor de 9 é 8 
# O sucessor de 9 é 10 

def valida_num_int():
    while True:
        try:
            num = int(input('\nInsira um número inteiro: '))
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
    
    return num


def mostra_antecessor(num):
    print(f'\nO antecessor de {num} é {num - 1}')


def mostra_sucessor(num):
    print(f'\nO sucessor de {num} é {num + 1}')


if __name__ == '__main__':
    num = valida_num_int()
    mostra_antecessor(num)
    mostra_sucessor(num)
    