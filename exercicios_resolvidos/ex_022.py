# 22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
# situação em relação ao alistamento militar. - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o 
# alistamento. - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do 
# alistamento. 
# idade limite de 0 - 100


def valida_ano_nascimento():
    while True:
        try:
            ano = int(input('Qual seu ano de nascimento: '))

            if ano <= 0:
                print('\n\033[mO ano de nascimento não pode ser igual a 0 ou inferior\033[m\n')
                continue

            idade = calcula_idade(ano)

            if idade > 100:
                print('\n\033[1;31mMeu fih tu já tá morto, limite de idade [0 - 100]\033[m\n')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um ano válido\033[m\n')
    
    return ano


def calcula_idade(ano_nascimento):
    from datetime import date

    data = date.today()
    ano_atual = data.year
    
    idade = ano_atual - ano_nascimento

    return idade


def situacao_alistamento(idade):
    if idade < 18:
        falta = 18 - idade
        resultado = f'Ainda falta {falta} anos para se alistar!\n'
    
    elif idade > 18:
        passou = idade - 18
        resultado = f'Já se passaram {passou} anos para se alistar, se aliste imediatamente!\n'
    
    else:
        resultado = f'Você esta na idade ideal para se alistar!\n'
    
    return resultado


def exibir_dados(ano_nascimento, idade, situacao):
    print('\n---- Dados ----\n')
    print(f'Ano nascimento: {ano_nascimento}\n'
          f'Idade: {idade} anos\n'
          f'Situação: {situacao}\n')


if __name__ == '__main__':
    ano_nascimento = valida_ano_nascimento()
    idade = calcula_idade(ano_nascimento)
    situacao = situacao_alistamento(idade)
    exibir_dados(ano_nascimento, idade, situacao)
