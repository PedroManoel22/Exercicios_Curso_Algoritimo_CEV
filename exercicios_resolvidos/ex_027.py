# 27) Crie um programa que leia duas notas de um aluno e calcule a sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO - Média 7.0 ou superior: APROVADO 

def valida_nota():
    while True:
        try:
            nota = float(input('Insira sua nota: '))

            if nota < 0:
                print('\n\033[1;33mA nota não pode ser negativa!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um nota válida!\033[m\n')
    
    return nota


calcula_media = lambda nota1, nota2: (nota1 + nota2) / 2


def situacao(media):
    if media <= 4.9:
        resposta = '\033[1;31mREPROVADO\033[m'
    
    elif media >= 5 and media <= 6.9:
        resposta = '\033[1;33mRECUPERAÇÃO\033[m'
    
    else:
        resposta = '\033[1;32mAPROVADO\033[m'

    print(f'Média = {media}\n'
          f'Situação: {resposta}\n')


if __name__ == '__main__':
    nota1 = valida_nota()
    nota2 = valida_nota()
    media = calcula_media(nota1, nota2)
    situacao(media)
