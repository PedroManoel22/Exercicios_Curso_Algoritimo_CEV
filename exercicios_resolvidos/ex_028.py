# 28) Faça um programa que leia a largura e o comprimento de um terreno 
# retangular, calculando e mostrando a sua área em m². O programa também 
# deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m² = TERRENO POPULAR - Entre 100m² e 500m² = TERRENO MASTER - Acima de 500m² = TERRENO VIP 

def valida_largura():
    while True:
        try:
            largura = float(input('Insira a largura do terreno: '))

            if largura <= 0:
                print('\n\033[1;33mNão é possível colocar largura igual a 0 ou menor!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque uma largura válida!\033[m\n')
    
    return largura


def valida_comprimento():
    while True:
        try:
            comprimento = float(input('Insira o comprimento do terreno: '))

            if comprimento <= 0:
                print('\n\033[1;33mNão é possível colocar comprimento igual a 0 ou menor!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um comprimento válido!\033[m\n')
    
    return comprimento

calcula_area = lambda lar, com: lar * com

def mostra_classificacao_terreno(area):
    if area < 100:
        classificacao = 'TERRENO POPULAR'
    
    elif area >= 100 and area <= 500:
        classificacao = 'TERRENO MASTER'
    
    else:
        classificacao = 'TERRENO VIP'
    
    print(f'Área do terreno: {area} m²\n'
          f'Classificação: {classificacao}\n')


if __name__ == '__main__':
    largura = valida_largura()
    comprimento = valida_comprimento()
    area = calcula_area(largura, comprimento)
    mostra_classificacao_terreno(area)