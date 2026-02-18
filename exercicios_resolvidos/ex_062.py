# 62) Faça um programa usando a estrutura “faça enquanto” que leia a idade de 
# várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou 
# não continuar a digitar dados. No final, quando o usuário decidir parar, mostre 
# na tela: 
# a) Quantas idades foram digitadas 
# b) Qual é a média entre as idades digitadas 
# c) Quantas pessoas tem 21 anos ou mais. 

from ex_053 import valida_idade
import numpy as np

idades = []
while True:
    idade = valida_idade()
    idades.append(idade)
    while True:
        continuar = input('Deseja continuar [S/N]? ').upper().strip()

        if continuar != 'S' and continuar != 'N':
            print('\n\033[1;31mPor favor insira uma opção válida!\033[m\n')
        
        else:
            break
    
    if continuar == 'N':
        break

qtd_pessoas = len(idades)
media_idade = np.mean(idades)
pessoas_21_ou_mais = filter(lambda x: x >= 21, idades)
pessoas_21_ou_mais = len(list(pessoas_21_ou_mais))

print('\n---- Dados ----\n')
print(f'Quatidade de pessoas: {qtd_pessoas}\n'
      f'Média de idade: {media_idade:.2f}\n'
      f'Pessoas com 21 anos ou mais: {pessoas_21_ou_mais}\n')
