# 16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um 
# fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele 
# já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule 
# quantos dias de vida um fumante perderá e exiba o total em dias. 

def qtd_cigarro_dias():
    while True:
        try:
            qtd = int(input('Insira a quantidade de cigarros que você fuma por dia: '))

            if qtd <= 0:
                print('\n\033[1;31mNão é possível colocar quantidade igual a 0 ou infeirior!\033[m\n')
                continue
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque uma quantidade válida\033[m\n')
    
    return qtd


def anos_fumando():
    while True:
        try:
            anos = int(input('Você fuma faz quantos anos? '))

            if anos <= 0:
                print('\n\033[mNão é possível colocar ano 0 ou inferior!\033[m\n')
                continue
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um ano válido\033[m\n')
    
    return anos


def reducao_tempo_vida(qtd, anos):
    perda = (qtd * 365 * anos) * 10
    dias_perda = perda / 60
    return dias_perda


def exibir_dados(qtd_por_dia, anos, dias):
    print(f'\nVocê fumou {qtd_por_dia} cigarros por dia durante {anos} anos\n'
          f'Com isso você teve uma redução de {dias:.2f} dias de vida!\n')


if __name__ == '__main__':
    qtd_cigarros = qtd_cigarro_dias()
    anos = anos_fumando()
    dias_perdidos = reducao_tempo_vida(qtd_cigarros, anos)
    exibir_dados(qtd_cigarros, anos, dias_perdidos)
    