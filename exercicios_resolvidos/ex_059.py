# 59) Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai 
# perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre: 
# a) qual é a maior idade lida 
# b) quantos homens foram cadastrados 
# c) qual é a idade da mulher mais jovem 
# d) qual é a média de idade entre os homens

from ex_053 import valida_idade, valida_sexo

if __name__ == '__main__':
    import numpy as np
    count = 1
    idades = []
    idades_mulheres = []
    idades_homens = []
    homens_cadastrados = 0

    while True:
        print(f'\n---- dados da {count}° pessoa ----\n')
        idade = valida_idade()
        sexo = valida_sexo()
        idades.append(idade)
        if sexo == 'M':
            homens_cadastrados += 1
            idades_homens.append(idade)
        
        elif sexo == 'F':
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
    

    print(f'\nMaior idade lida: {max(idades)}\n'
          f'Quantidade de homens: {homens_cadastrados}\n'
          f'Idade da mulher mais jovem: {min(idades_mulheres)}\n'
          f'Média de idade entre os homens: {np.mean(idades_homens)}\n')
    
