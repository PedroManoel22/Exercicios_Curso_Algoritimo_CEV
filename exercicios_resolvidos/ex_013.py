# 13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o 
# seu novo salário, com 15% de aumento. 

def valida_salario():
    while True:
        try:
            salario = float(input('Digite o seu salário atual: '))
            if salario <= 0:
                print('\n\033[1;31Não existe salario de R$0 ou inferior\033[m\n')

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número válido!\n\033[m')
    
    return salario


def reajuste_salario(salario, reajuste):
    novo_salario = salario + ((reajuste / 100) * salario)
    return novo_salario


def exibir_dados(salario_antigo, salario_reajustado):
    print(f'\nSalário antigo: {salario_antigo}\n'
          f'Salário reajustado com 15% de aumento: {salario_reajustado}\n')


if __name__ == '__main__':
    AUMENTO = 15
    salario = valida_salario()
    salario_reajustado = reajuste_salario(salario, AUMENTO)
    exibir_dados(salario, salario_reajustado)
    