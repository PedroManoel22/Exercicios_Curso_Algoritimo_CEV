# 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua 
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou 
# não um bom aproveitamento (se ficou acima da média 7.0).
# nota < 5 reprovado, nota >= 5 and nota <= 6.9 recuperação, nota >= 7 aprovado 

def pede_valida_nome():
    # valida o nome
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


def pede_valida_notas():
    # valida a primeira nota
    while True:
        try:
            nota1 = float(input('Insira a primeira nota: '))
            
            if nota1 < 0:
                print('\n\033[1;35mA nota miníma é 0, não aceitamos notas negativas!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque uma nota válida!\033[m\n')
    
    # valida a segunda nota
    while True:
        try:
            nota2 = float(input('Insira a segunda nota: '))
            
            if nota1 < 0:
                print('\n\033[1;35mA nota miníma é 0, não aceitamos notas negativas!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque uma nota válida!\033[m\n')
    
    return nota1, nota2 


def calcula_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


def situacao_aluno(media):
    if media < 5:
        situacao = '\033[1;31mReprovado\033[m'
        
    elif media >= 5 and media <= 6.9:
        situacao = '\033[1;33mRecuperação\033[m'
        
    else:
        situacao = '\033[1;32mAprovado\033[m'
    
    return situacao


def exibir_dados(nome, nota1, nota2, media, situacao):
    print('\n---- Situação do aluno ----')
    print(f'Aluno: {nome}\n'
          f'Primeira nota: {nota1}\n'
          f'Segunda nota: {nota2}\n'
          f'Média: {media}\n'
          f'Situação {situacao}\n')


if __name__ == '__main__':
    nome = pede_valida_nome()
    notas = pede_valida_notas()
    media = calcula_media(*notas)
    situacao = situacao_aluno(media)
    exibir_dados(nome, *notas, media, situacao)