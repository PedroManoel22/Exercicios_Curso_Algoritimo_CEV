# 37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um 
# aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, 
# o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. 
# No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres - menos de 15 anos de empresa: +5% 
# - de 15 até 20 anos de empresa: +12% 
# - mais de 20 anos de empresa: +23% 
# - Homens - menos de 20 anos de empresa: +3% 
# - de 20 até 30 anos de empresa: +13% 
# - mais de 30 anos de empresa: +25% 

def valida_salario_atual():
    while True:
        try:
            salario = float(input('Insira seu salário atual: '))

            if salario <= 0:
                print('\n033[1;31mPor favor coloque um salário acima de R$0.00!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um salário válido!\033[m\n')
    
    return salario


def valida_sexo():
    sexos = ['F', 'M']

    while True:
        sexo = input('Insira seu gênero, [F/M]: ').upper().strip()

        if sexo not in sexos:
            print('\n\033[1;31mPor favor coloque um gênero F ou M\033[m\n')
            continue

        break

    return sexo
            

def valida_anos_trabalhando():
    while True:
        try:
            anos = int(input('Insira quantos anos você trabalha: '))

            if anos <= 0:
                print('\n033[1;31mPor favor coloque um anop acima de 0!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um ano válido!\033[m\n')
    
    return anos


def calcula_reajuste_salarial(salario, genero, anos):
    if genero == 'F':
        if anos < 15:
            reajuste = salario + (salario * 0.05)
            porcentagem = 5
        
        elif anos >= 15 and anos <= 20:
            reajuste = salario + (salario * 0.12)
            porcentagem = 12
        
        else:
            reajuste = salario + (salario * 0.23)
            porcentagem = 23
    
    if genero == 'M':
        if anos < 20:
            reajuste = salario + (salario * 0.03)
            porcentagem = 3

        elif anos >= 20 and anos <= 30:
            reajuste = salario + (salario * 0.13)
            porcentagem = 13
        
        else:
            reajuste = salario + (salario * 0.25)
            porcentagem = 25
    
    return reajuste, porcentagem


def exibir_dados(salario, genero, anos, reajuste, porcentagem):
    print('\n---- Dados ----\n')
    print(f'Salário: R${salario:.2f}\n'
          f'Gênero: {genero}\n'
          f'Anos trabalhados: {anos}\n'
          f'Porcentagem do reajuste: {porcentagem}%\n'
          f'Salário reajustado: R${reajuste:.2f}\n')  


if __name__ == '__main__':
    salario = valida_salario_atual()
    genero = valida_sexo()
    anos = valida_anos_trabalhando()
    reajuste = calcula_reajuste_salarial(salario, genero, anos)
    exibir_dados(salario, genero, anos, *reajuste)
