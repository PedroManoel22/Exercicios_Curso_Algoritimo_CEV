# 14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
# um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
# sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

def kms_percorridos():
    while True:
        try:
            kms = float(input('Insira a quantidade de Kms percorridos: '))

            if kms <= 0:
                print('\n\033[1;31mÉ impossível percorrer 0 ou Kms negativos\033[m\n')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor uma quantidade de kms válida\033[m\n')
    
    return kms


def quantidade_dias():
    while True:
        try:
            dias = int(input('Insira a quantidade de dias que você ficou com o carro: '))

            if dias <= 0:
                print('\n\033[1;31mÉ impossível alugar o carro por 0 dias ou dias negativos')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor uma quantidade de dias válida\033[m\n')
    
    return dias


def custo_alocagem(kms_percorridos, dias):
    custo_dias = 90 * dias
    custo_kms = kms_percorridos * 0.2
    custo_final = custo_dias + custo_kms
    return custo_final


def exibir_dados(kms_percorridos, dias, custo_final):
    print(f'\nForam percorridos {kms_percorridos}Kms em {dias} dias\n'
          f'O custo total da alocagem do carro foi de R${custo_final}\n')


if __name__ == '__main__':
    kms = kms_percorridos()
    dias = quantidade_dias()
    custo_final = custo_alocagem(kms, dias)
    exibir_dados(kms, dias, custo_final)