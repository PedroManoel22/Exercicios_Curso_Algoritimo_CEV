# 35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O 
# aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para 
# carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa 
# que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e 
# quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a 
# tabela a seguir: 
# Carros populares (aluguel de R$90 por dia) 
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km 
# Carros de luxo (aluguel de R$150 por dia) 
# - Até 200Km percorridos: R$0,30 por Km 
# - Acima de 200Km percorridos: R$0,25 por Km 

def tipo_carro():
    print('\n[1] - Carro popular\n'
          '[2] - Carro de luxo\n')
    
    opcoes = [1, 2]
    
    while True:
        try:
            tipo = int(input('\nInsira o tipo do carro: '))

            if tipo not in opcoes:
                print('\n\033[mColoque um tipo de carro existente!, popular ou de luxo!\n\033[m')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um tipo válido!\033[m\n')
    
    return tipo


def dias_alugados():
    while True:
        try:
            dias = int(input('Por quantos dias o carro foi alugado? '))

            if dias <= 0:
                print('\n\033[1;31mNão é possível colocar dias igual a 0 ou negativos!\033[m\n')
                continue
                
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número válido!\033[m\n')
    
    return dias


def kms_percorridos():
    while True:
        try:
            kms = float(input('Insira quantos Kms foram percorridos: '))
            if kms <= 0:
                print('\n033[1;31mPor favor coloque uma valor maior que 0')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque uma distância válida!\033[m\n')
    
    return kms


def calcular_custo(tipo, dias, kms):
    if tipo == 1 and kms <= 100:
        custo = (90 * dias) + (kms * 0.2)
    
    elif tipo == 1 and kms > 100:
        custo = (90 * dias) + (kms * 0.1)
    
    elif tipo == 2 and kms <= 200:
        custo = (150 * dias) + (kms * 0.3)
    
    elif tipo == 2 and kms > 200:
        custo = (150 * dias) + (kms * 0.25)
    
    return custo


def exibir_dados(tipo, dias, kms, custo):
    if tipo == 1:
        tipo = 'Popular'

    else:
        tipo = 'Luxo'

    print('\n---- Dados ----\n')
    print(f'Tipo: {tipo}\n'
          f'Dias alugados: {dias} dias\n'
          f'Kms percorridos: {kms:.2f} Km\n'
          f'Custo: R${custo:.2f}\n')


if __name__ == '__main__':
    tipo = tipo_carro()
    dias = dias_alugados()
    kms = kms_percorridos()
    custo = calcular_custo(tipo, dias, kms)
    exibir_dados(tipo, dias, kms, custo)
