# 23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos 
# para todos, mas especialmente para mulheres. Faça um programa que leia nome, 
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo 
# que: - Homens ganham 5% de desconto - Mulheres ganham 13% de desconto 

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


def valida_sexo():
    while True:
        sexo = input('Insira o sexo [H/M]: ').upper().strip()

        if sexo not in 'MH' or not sexo:
            print('\n\033[1;31mPor favor coloque um sexo válido!\033[m\n')
        
        else:
            break

    return sexo


def valida_valor_compras():
    while True:
        try:
            valor = float(input('Insira o valor das compras: '))
            
            if valor <= 0:
                print('\n\033[1;35mNão é possível colocar valor igual a 0 ou inferior\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um valor válido!\033[m\n')
    
    return valor


def calcula_desconto(sexo, valor_compras):
    if sexo == 'H':
        desconto = valor_compras - (valor_compras * 0.05)
    
    else:
        desconto = valor_compras - (valor_compras * 0.13)
    
    return desconto


def exibir_dados(nome, sexo, valor_compras, valor_desconto):
    if sexo == 'H':
        desconto = 5
    
    else:
        desconto = 13

    print('\n---- Nota Fiscal ----\n')
    print(f'Nome: {nome}\n'
          f'Valor: R${valor_compras}\n'
          f'Desconto: {desconto}%\n'
          f'Preço final: \033[32mR${valor_desconto}\033[m\n')


if __name__ == '__main__':
    nome = valida_nome()
    sexo = valida_sexo()
    valor = valida_valor_compras()
    desconto = calcula_desconto(sexo, valor)
    exibir_dados(nome, sexo, valor, desconto)
