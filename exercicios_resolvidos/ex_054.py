# 54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando 
# no final: 
# a) Qual foi a média de altura do grupo 
# b) Quantas pessoas pesam mais de 90Kg 
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m 
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg. 
from ex_034 import valida_peso, valida_altura

if __name__ == '__main__':
    TOTAL_PESSOAS = 7
    total_altura = 0
    pessoas_acima_90kg = 0
    pessoas_abaixo_50kg_menor_1_60 = 0
    pessoas_acima_1_90_mais_100kg = 0

    for i in range(1, TOTAL_PESSOAS + 1):
        print(f'\n---- Insira os dados da {i}° pessoa ----\n')

        peso = valida_peso()

        if peso > 90:
            pessoas_acima_90kg += 1

        altura = valida_altura()

        total_altura += altura

        if peso < 50 and altura < 1.6:
            pessoas_abaixo_50kg_menor_1_60 += 1
        
        if altura > 1.9 and peso > 100:
            pessoas_acima_1_90_mais_100kg += 1

        
    
    altura_media = total_altura / TOTAL_PESSOAS

    # mostrar dados

    print('\nResultado\n'
          f'Altura média do grupo: {altura_media:.2f}\n'
          f'Quantas pessoas pensam mais de 90Kg: {pessoas_acima_90kg}\n'
          f'Quantas pessoas pesam menos de 50Kg e tem menos de 1.60m: {pessoas_abaixo_50kg_menor_1_60}\n'
          f'Quantas pessoas medem mais de 1.90 e pesam mais de 100Kg: {pessoas_acima_1_90_mais_100kg}\n')

