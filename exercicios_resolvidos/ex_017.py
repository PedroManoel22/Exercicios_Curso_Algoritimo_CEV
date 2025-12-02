# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba 
# o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida. 

def valida_velocidade():
    while True:
        try:
            velocidade = float(input('Qual a velocidade do carro? '))

            if velocidade <= 0:
                print('\n\033[mNão é possível colocar uma velocidade igual a 0 ou infeirior!\033[m\n')
                continue
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque uma velocidade válida\033[m\n')
    
    return velocidade


def leva_multa_ou_nao(velocidade):
    if velocidade > 80:
        print('\n\033[1;31mVocê ultrapassou o limite de velocidade de 80Km/h\033[m\n')
        print(f'Velocidade registrada \033[1;31m{velocidade}Km/h\033[m\n')
        multa = (velocidade - 80) * 5
        print(f'Sua multa foi de R${multa}\n')
    
    else:
        print('\n\033[1;32mVocê está no limite da via\033[m\n')
        print(f'Velocidade registrada: {velocidade}Km/h\n')

if __name__ == '__main__':
    velocidade = valida_velocidade()
    leva_multa_ou_nao(velocidade)