# 34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no 
# peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o 
# indivíduo dentro de certas faixas. - abaixo de 18.5: Abaixo do peso - entre 18.5 e 25: Peso ideal - entre 25 e 30: Sobrepeso - entre 30 e 40: Obesidade - acima de 40: Obseidade mórbida 
# Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado 
# da altura) 
# A maior altura já registrada foi de 2,72 até 2025 por Robert Wadlow., então vamos considerar esta a altura maxima 

def valida_peso():
    while True:
        try:
            peso = float(input('Insira o seu peso: '))
            if peso <= 0:
                print('\n033[1;31mPor favor coloque um valor maior que 0.00Kg')
                continue

            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um peso válido!\033[m\n')
    
    return peso


def valida_altura():
    while True:
        try:
            altura = float(input('Insira a sua altura: '))
            if altura <= 0:
                print('\n\033[1;31mPor favor coloque uma valor maior que 0\033[m\n')
                continue

            if altura > 2.72:
                print('\n\033[1;31mPor favor coloque uma altura menor que 2.72m\033[m\n')
                continue
            
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque uma altura válida!\033[m\n')
    
    return altura


def calcular_IMC(peso, altura):
    imc = peso / (altura * altura)
    return imc


def classificacao_imc(imc):
    if imc < 18.5:
        resultado = 'Abaixo do peso'
    
    elif imc >= 18.5 and imc < 25:
        resultado = 'Peso ideal'
    
    elif imc >= 25 and imc < 30:
        resultado = 'Sobrepeso'
    
    elif imc >= 30 and imc < 40:
        resultado = 'Obesidade'
    
    else:
        resultado = 'Obesidade mórbida'
    
    return resultado


def exibir_dados(peso,altura, imc, classificacao):
    print('\n---- Dados ----\n')
    print(f'Peso: {peso}\n'
          f'Altura: {altura}\n'
          f'IMC: {imc:.2f}\n'
          f'Classificação: {classificacao}\n')
    
if __name__ == '__main__':
    peso = valida_peso()
    altura = valida_altura()
    imc = calcular_IMC(peso, altura)
    classificacao = classificacao_imc(imc)
    exibir_dados(peso, altura, imc, classificacao)
    