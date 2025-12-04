# 21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não 
# BISSEXTO. 

def valida_ano():
    while True:
        try:
            ano = int(input('Insira um ano, para saber se este é bissexto ou não: '))
            break
        
        except (ValueError, KeyboardInterrupt):
            print('\n\033[1;31mPor favor coloque um ano válido\033[m\n')
        
        except Exception as e:
            print(f'\n\033[1;33mError inesperado: {e.__class__.__name__}\033[m\n')
    
    return ano


def e_bissexto(ano):
    if ano % 4 == 0 or ano % 400 == 0:
        resultado = f'\nO ano de {ano} é bissexto!\n'
    
    else:
        resultado = f'\nO ano de {ano} NÃO é bissexto!\n'
    
    return resultado


if __name__ == '__main__':
    ano = valida_ano()
    print(e_bissexto(ano))