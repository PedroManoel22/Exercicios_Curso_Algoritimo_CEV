# 33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra 
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e 
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que 
# ela não pode exceder 30% do salário ou então o empréstimo será negado. 

def valida_valor_casa():
    while True:
        try:
            valor = float(input('Insira o valor da casa: '))
            if valor <= 0:
                print('\n033[1;31mPor favor coloque um valor maior que R$0.00')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um valor válido!\033[m\n')
    
    return valor


def valida_salario():
    while True:
        try:
            salario = float(input('Insira o seu salário: '))
            if salario <= 0:
                print('\n\033[1;31mPor favor coloque um valor maior que R$0.00\033[m\n')
                continue

            break

        except ValueError:
            print('\n033[1;31mPor favor coloque um valor válido!')
    
    return salario

    
def quantos_anos_quitar():
    while True:
        try:
            anos = int(input('Em quantos anos deseja quitar? '))
            if anos <= 0:
                print('\n\033[1;31mPor favor coloque um valor maior que 0 anos\033[m\n')
                continue

            break

        except ValueError:
            print('\n033[1;31mPor favor coloque um valor válido!')
    
    return anos


def calcular_valida_prestacao_mensal(valor_casa, salario, anos):
    prestacao = valor_casa / (anos * 12)
    trinta_por_cento = salario * 0.3
    if prestacao > trinta_por_cento:
        resultado = '\033[1;31mNegado\033[m' 
    else:
        resultado = '\033[1;32mAprovado\033[m' 
    
    return prestacao, resultado


def exibir_dados(valor_casa, salario, anos, prestacao, resultado):
    print('\n---- Dados ----\n')
    print(f'Valor do imóvel: R${valor_casa}\n'
          f'Salário: R${salario}\n'
          f'Prazo para quitar: {anos} anos\n'
          f'Valor da prestação: R${prestacao:.2f}\n'
          f'Resultado do empréstimo: {resultado}\n')


if __name__ == '__main__':
    valor_casa = valida_valor_casa()
    salario = valida_salario()
    anos = quantos_anos_quitar()
    prestacao = calcular_valida_prestacao_mensal(valor_casa, salario, anos)
    exibir_dados(valor_casa, salario, anos, *prestacao)