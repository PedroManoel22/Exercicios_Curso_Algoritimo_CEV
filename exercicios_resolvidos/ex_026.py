# 26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando 
# na tela uma das mensagens abaixo: - O primeiro valor é o maior - O segundo valor é o maior - Não existe valor maior, os dois são iguais 

def valid_nums_int():
    while True:
        try:
            num = int(input('Insira um número inteiro: '))

            if num <= 0:
                print('\nInsira número maior que zero!\n')
                continue
        
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
    return num


def comparison_of_numbers(num1, num2):
    if num1 > num2:
        response = f'\nO primeiro valor é o maior\n'
    
    elif num2 > num1:
        response = f'\nO segundo valor é o maior\n'
    
    else:
        response = '\nNão existe valor maior, os dois são iguais\n'
    
    return response


if __name__ == '__main__':
    num1 = valid_nums_int()
    num2 = valid_nums_int()
    response = comparison_of_numbers(num1, num2)
    print(response)
