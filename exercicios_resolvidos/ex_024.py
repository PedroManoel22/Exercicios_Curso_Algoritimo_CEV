# 24) Faça um algoritmo que pergunte a distância que um passageiro deseja 
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para 
# viagens até 200Km e R$0.45 para viagens mais longas.

def valida_distancia():
    while True:
        try:
            distancia = float(input('Insira a distância que deseja pecorrer em Km: '))
            
            if distancia <= 0:
                print('\n\033[1;35mNão é possível colocar uma distância igual a 0 ou inferior\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um valor válido!\033[m\n')
    
    return distancia


def calcula_preco_passagem(distancia):
    if distancia <= 200:
        preco = round(distancia * 0.5, 2)

    else:
        preco = round(distancia * 0.45, 2)
    
    return preco


def exibir_dados(distancia, preco):
    print('\n---- Dados da viagem ----\n')
    print(f'Sua viagem foi um total de {distancia} km\n'
          f'Com isso sua viagem irá custar R${preco}\n')
    

if __name__ == '__main__':
    distancia = valida_distancia()
    preco = calcula_preco_passagem(distancia)
    exibir_dados(distancia, preco)