# 3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no 
# final uma mensagem. 
# Ex: 
# Nome do Funcionário: Maria do Carmo 
# Salário: 1850,45 
# O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho. 

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


def valida_salario(nome):
    while True:
        try:
            salario = float(input(f'Insira o salario do funcionário {nome}: '))
            break
        
        except ValueError:
            print('\n\033[1;31mPor favor insira um salário válido\033[m\n')
            
    return salario


def mostra_dados(nome, salario):
    print(f'\nNome do funcionário: {nome}\n'
          f'Salário: {salario:.2f}\n'
          f'O funcionário {nome} tem um salário de R${salario:.2f} em junho!\n')


if __name__ == '__main__':
    nome = valida_nome()
    salario = valida_salario(nome)
    mostra_dados(nome, salario)
   