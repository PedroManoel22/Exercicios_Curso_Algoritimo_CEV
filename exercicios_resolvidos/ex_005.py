# 5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre 
# na tela a sua média na disciplina. 
# Ex:  
# Nota 1: 4.5 
# Nota 2: 8.5 
# A média entre 4.5 e 8.5 é igual a 6.5 

def valida_notas():
    # Valida a primeria nota
    while True:
        try:
            nota1 = float(input('Insira a primeira nota: '))
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque uma nota válida\033[m\n')

    # valida a segunda nota
    while True:
        try:
            nota2 = float(input('Insira a segunda nota: '))
            break
            
        except ValueError:
            print('\n\033[1;31mPor favor coloque uma nota válida\033[m\n')
            
    
    return mostra_media(nota1, nota2)

def mostra_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f'\nA média entre {nota1:.1f} e {nota2:.1f} é igual a {media:.1f}\n')

if __name__ == '__main__':
    notas = valida_notas()
    