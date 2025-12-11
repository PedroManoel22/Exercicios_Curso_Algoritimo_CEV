# 36) Um programa de vida saudável quer dar pontos atividades físicas que podem 
# ser trocados por dinheiro. O sistema funciona assim: - Cada hora de atividade física no mês vale pontos
# - até 10h de atividade no mês: ganha 2 pontos por hora - 
# de 10h até 20h de atividade no mês: ganha 5 pontos por hora - acima de 20h de atividade no mês: ganha 10 pontos por hora
#  - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)   
# Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, 
# calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.

def valida_horas():
    while True:
        try:
            horas = int(input('\nInsira quantas horas você fez atividades físicas neste mês: '))
            if horas <= 0:
                print('\n\033[mColoque uma hora maior que 0!\033[m\n')
            
            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque uma hora válida!\033[m\n')
        
    return horas


def calcula_pontos(horas):
    if horas < 10:
        pontos = horas * 2
    
    elif horas >= 10 and horas <= 20:
        pontos = horas * 5
    
    else:
        pontos = horas * 10
    
    return pontos


def converte_pontos_para_dinheiro(pontos):
    premio = pontos * 0.05
    return premio


def exibir_dados(horas, pontos, premio):
    print('\n---- Resultado ----\n')
    print(f'Horas de atividade física: {horas}h\n'
          f'Pontos: {pontos}\n'
          f'Premio: R${premio}\n')
                 

if __name__ == '__main__':
    horas = valida_horas()
    pontos = calcula_pontos(horas)
    premio = converte_pontos_para_dinheiro(pontos)
    exibir_dados(horas, pontos, premio)
    