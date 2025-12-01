# 7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a 
# sua terça parte. 
# Ex:  
# Digite um número: 3.5 
# O dobro de 3.5 é 7.0 
# A terça parte de 3.5 é 1.16666 

def valida_num():
    while True:
        try:
            num = float(input('Insira um número real: '))
            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número real!\n\033[m')
    
    return num


def dobro_terca_parte(num):
    dobro = num * 2
    terca_parte = round(num / 3, 5)
    print(f'O dobro de {num} é {dobro}\n'
          f'A terça parte de {num} é {terca_parte}')


if __name__ == '__main__':
    num = valida_num()
    dobro_terca_parte(num)
