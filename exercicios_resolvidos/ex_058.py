# 58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa 
# vai parar quando for digitada a idade 999. No final, mostre quantos alunos 
# existem na turma e qual é a média de idade do grupo. 

from ex_053 import valida_idade

if __name__ == '__main__':
    count = 1
    total_idades = 0

    while True:
        
        print(f'\n---- dados do {count}° aluno [digite 999 para cancelar] ---- \n')
        idade = valida_idade()
        if idade != 999:
            count += 1
            total_idades += idade

        else:
            break
    
    count -= 1
    media_idade = total_idades / count

    print(f'\nTotal de alunos: {count}\n'
          f'Idade média: {media_idade:.2f}\n')
    