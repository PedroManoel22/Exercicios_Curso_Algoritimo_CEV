# 18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade 
# dela e depois mostre se ela pode ou não votar. 
# Considerando a idade maxima de 100 anos de idade
# Neste exercício consideramos que para ser apto a votar
# a pessoa tem que ter uma idade entre 16 a 80, fora disso ela não vota

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


def vota_ou_nao_vota(idade):
    if idade >= 16 and idade <= 80:
        print(f'\nCom {idade} anos você:')
        print('\nPode votar!\n')
    
    else:
        print('\nNão pode votar')


if __name__ == '__main__':
    ano_nascimento = valida_ano_nascimento()
    idade = calcula_idade(ano_nascimento)
    vota_ou_nao_vota(idade)
    