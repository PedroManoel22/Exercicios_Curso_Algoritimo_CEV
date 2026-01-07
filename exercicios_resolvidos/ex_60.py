# 60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. 
# O programa vai perguntar se o usuário quer ou não continuar. No final, mostre: 
# a) O nome da pessoa mais velha 
# b) O nome da mulher mais jovem 
# c) A média de idade do grupo 
# d) Quantos homens tem mais de 30 anos 
# e) Quantas mulheres tem menos de 18 anos 

from ex_053 import valida_idade, valida_sexo
from ex_029 import valida_nome

if __name__ == '__main__':
    import numpy as np

    count = 1
    nomes = []
    idades = []
    nomes_homens = []
    nomes_mulheres = []
    idades_homens = []
    idades_mulheres = []


    while True:
        print(f'\n---- dados da {count}° pessoa ----\n')
        nome = valida_nome()
        idade = valida_idade()
        sexo = valida_sexo()

        nomes.append(nome)
        idades.append(idade)

        if sexo == 'M':
            nomes_homens.append(nome)
            idades_homens.append(idade)
        
        elif sexo == 'F':
            nomes_mulheres.append(nome)
            idades_mulheres.append(idade)       

        while True:
            continuar = input('Deseja continuar [S/N]? ').upper().strip()

            if continuar != 'S' and continuar != 'N':
                print('\n\033[1;31mPor favor insira uma opção válida!\033[m\n')
            
            else:
                count += 1
                break

        if continuar == 'N':
            break
    
    nome_maior_idade = nomes[idades.index(max(idades))]
    mulher_mais_jovem = nomes_mulheres[idades_mulheres.index(min(idades_mulheres))]
    media_idade = np.mean(idades)
    homens_com_mais_30 = filter(lambda x: x > 30, idades_homens)
    homens_com_mais_30 = len(list(homens_com_mais_30))
    mulheres_com_menos_18 = filter(lambda x: x < 18, idades_mulheres)
    mulheres_com_menos_18 = len(list(mulheres_com_menos_18))

    # dados
    print('\n---- Dados ----\n')
    print(f'\nNome da pessoa mais velha: {nome_maior_idade}\n'
          f'Nome da mulher mais jovem: {mulher_mais_jovem}\n'
          f'Média de idade do grupo: {media_idade} anos\n'
          f'Quantidade de homens com mais de 30 anos: {homens_com_mais_30}\n'
          f'Quantidade de mulheres com menos de 18 anos: {mulheres_com_menos_18}\n')
