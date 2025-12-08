# 29) Desenvolva um programa que leia o nome de um funcionário, seu salário, 
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de 
# acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3% - entre 3 e 10 anos: aumento de 12.5% - 10 anos ou mais: aumento de 20%

def valida_nome():
    while True:
        try:
            nome = input('Qual é o seu nome? ')
            e_num = nome.isdigit()
            tamanho = len(nome)


            if not nome or e_num or tamanho <= 2: 
                print('\n\033[1;31mPor favor coloque um nome\033[m\n')

            else:
                break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um nome válido!\033[m\n')
    
    return nome


def valida_salario():
    while True:
        try:
            salario = float(input('Insira o valor do seu salário: '))

            if salario <= 0:
                print('\n\033[1;33mNão é possível colocar salário igual a 0 ou menor!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um salário válido!\033[m\n')
    
    return salario


def valida_anos_trabalhados():
    while True:
        try:
            anos = int(input('Quantos anos você trabalha na empresa: '))

            if anos <= 0:
                print('\n\033[1;31mPor favor coloque um ano válido!\033[m\n')
                continue
            
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um ano válido!\033[m\n')
    
    return anos
            

def reajuste_salarial(anos_trabalhados, salario):
    if anos_trabalhados < 3:
        porcentual = 3
        reajuste = salario + (salario * 0.03)
    
    elif anos_trabalhados >= 3 and anos_trabalhados <= 10:
        porcentual = 12.5
        reajuste = salario + (salario * 0.125 )
    
    else:
        porcentual = 20
        reajuste = salario + (salario * 0.2)
    
    return reajuste, porcentual


def exibir_dados(nome, salario_antigo, anos_trabalhados, salario_reajustado, porcentual):
    print(f'\n---- Dados do Funcionário ----\n')
    print(f'Nome: {nome}\n'
          f'Salário atual: R${salario_antigo}\n'
          f'Anos na empresa: {anos_trabalhados}\n'
          f'Salário com aumento de {porcentual}% = R${salario_reajustado}\n')


if __name__ == '__main__':
    nome = valida_nome()
    salario = valida_salario()
    anos = valida_anos_trabalhados()
    reajuste = reajuste_salarial(anos, salario)
    exibir_dados(nome, salario, anos, *reajuste)
    