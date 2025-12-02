# 15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o 
# salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 
# por hora trabalhada. 

def dias_trabalhados():
    while True:
        try:
            dias = int(input('Insira a quantidade de dias trabalhados: '))

            if dias <= 0:
                print('\n\033[mNão é possível colocar dias 0 ou inferiores!\033[m\n')
                continue
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque uma quantidade válida\033[m\n')
    
    return dias


def calcula_salario(dias):
    horas_trabalhadas = dias * 8
    salario = horas_trabalhadas * 25
    return horas_trabalhadas, salario


def exibir_dados(dias, horas_trabalhadas, salario):
    print(f'\nForam {dias} dias trabalhados\n'
          f'Contabilizando ao total {horas_trabalhadas} horas trabalhadas\n'
          f'Com isso o salário foi de R${salario}\n')


if __name__ == '__main__':
    dias = dias_trabalhados()
    salario = calcula_salario(dias)
    exibir_dados(dias, *salario)
    
