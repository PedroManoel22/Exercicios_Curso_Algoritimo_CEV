# 20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou 
# ÍMPAR. 

def valida_num_int():
    while True:
        try:
            num = int(input('Insira um número inteiro: '))
            break
        
        except (ValueError, KeyboardInterrupt):
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
        
        except Exception as e:
            print(f'\n\033[1;33mError inesperado: {e.__class__.__name__}\033[m\n')
    
    return num


def par_impar(num):
    if num % 2 == 0:
        resultado = 'Par'
    
    else:
        resultado = 'Ímpar'
    
    return resultado


def exibir_dados(num, resultado):
    print(f'\nO número {num}\n'
          f'É {resultado}\n')


if __name__ == '__main__':
    num = valida_num_int()
    resultado = par_impar(num)
    exibir_dados(num, resultado)
