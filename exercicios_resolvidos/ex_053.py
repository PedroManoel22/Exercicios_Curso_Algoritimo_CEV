# 53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final: 
# a) Quantos homens foram cadastrados 
# b) Quantas mulheres foram cadastradas 
# c) A média de idade do grupo 
# d) A média de idade dos homens 
# e) Quantas mulheres tem mais de 20 anos 

def valida_sexo():
    while True:
        sexo = input('Insira o sexo [M/F]: ').upper().strip()
        
        if sexo in ('M', 'F'):
            return sexo
        
        else:
            print('\n\033[1;31mPor favor coloque um sexo válido!\033[m\n')
            continue


def valida_idade():
    while True:
        try:
            idade = int(input('Insira a idade: '))

            if idade <= 0:
                print('\n\033[1;33mNão é possível colocar idade igual a 0 ou menor!\033[m\n')
                continue

            return idade
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um idade válida!\033[m\n')
    



if __name__ == '__main__':
    import numpy
    idades = []
    sexos = []
    idades_homens = []
    qtd_mulheres_acima_vinte = 0

    for i in range(1, 6):
        print(f'\n---- Dados da {i}° pessoa ----\n')
        idade = valida_idade()
        sexo = valida_sexo()
        if sexo == 'M':
            idades_homens.append(idade)
        
        elif sexo == 'F' and idade > 20:
            qtd_mulheres_acima_vinte += 1

        idades.append(idade)
        sexos.append(sexo)
    
    homens_cadastrados = sexos.count('M')
    mulheres_cadastradas = sexos.count('F')
    media_idade = numpy.mean(idades)
    media_idade_homens = numpy.mean(idades_homens)

    # menu 

    print('\n**** Resultado ****\n')
    print(f'Homens Cadatrados: {homens_cadastrados}\n'
          f'Mulheres Cadastradas: {mulheres_cadastradas}\n'
          f'Média de idade do grupo: {media_idade:.2f} anos\n'
          f'Média de idade dos homens: {media_idade_homens:.2f} anos\n'
          f'Quantas mulheres tem mais de 20 anos: {qtd_mulheres_acima_vinte}\n')
