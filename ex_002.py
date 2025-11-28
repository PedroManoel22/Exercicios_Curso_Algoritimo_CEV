# 2) Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas
# vindas para ela: 
# Ex: 
# Qual é o seu nome? João da Silva 
# Olá João da Silva, é um prazer te conhecer!

def valida_nome():
    while True:
        try:
            nome = input('Qual é o seu nome? ')
            e_num = nome.isdigit()
            tamanho = len(nome)


            if not nome or e_num or tamanho <= 2: 
                print('\n\033[1;31mPor favor coloque um nome\033[m\n')

            else:
                break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um nome válido!\033[m\n')
    
    return nome


def escreve_msg(nome):
    return f'Olá {nome}, é um prazer te conhecer!'


if __name__ == '__main__':
    nome = valida_nome()
    msg = escreve_msg(nome)
    print(msg)
