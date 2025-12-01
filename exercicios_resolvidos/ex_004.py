# 4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório 
# entre eles. 
# Ex: 
# Digite um valor: 8 
# Digite outro valor: 5 
# A soma entre 8 e 5 é igual a 13. 

def valida_numeros():
    # Valida primeiro número
    while True:
        try:
            x = int(input('Insira o primeiro número: '))
            break
            
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')

    # Valida segundo número   
    while True:
        try:
            y = int(input('Insira o segundo número: '))
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
    
    return soma(x, y)


def soma(x, y):
    print(f'\nA soma entre {x} e {y} é igual a {x + y}')


if __name__ == '__main__':
    numeros = valida_numeros()
    
