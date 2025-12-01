# 10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

def valida_area():
    # Valida largura
    while True:
        try:
            largura = float(input('Insira a largura da sua parede: '))
            if largura <= 0:
                print('\nA largura não pode ser igual a 0 ou menor!\n')
                continue

            break
            
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número válido\033[m\n')

    # Valida altura
    while True:
        try:
            altura = float(input('Insira a altura da sua parede: '))
            if altura <= 0:
                print('\nA altura não pode ser igual a 0 ou menor!\n')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número válido\033[m\n')
    
    return calcula_area(largura, altura)


def calcula_area(largura, altura):
    area = largura * altura
    return quantidade_tinta(area)


def quantidade_tinta(area):
    qtd_tinta = area / 2
    print(f'Area da parede: {area}m²')
    print(f'\nPara pintarmos sua parede precisamos de {qtd_tinta} litros de tinta!')


if __name__ == '__main__':
    valores = valida_area()
