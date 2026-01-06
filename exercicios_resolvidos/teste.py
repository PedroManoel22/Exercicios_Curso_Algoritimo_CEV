# print('João pessoa')
# from random import randint

# jogada_nomes = ['Pedra', 'Papel', 'Tesoura']

# jogada = randint(1,4)
# print(jogada)


def teste(string):
    verificacao = []
    if len(string) > 26:
        return 'Sua string deve ter no maximo 26 caracteres!'

    for l in string:
        if l not in verificacao:
            verificacao.append(l)
    
    if ''.join(verificacao) == string:
        string = ''.join(sorted(string))
        return string
    
    if verificacao != string:
        print(verificacao)
        return 'Sua string deve haver apenas caracteres unicos!'



if __name__ == '__main__':
    teste1 = 'lkjhgfdsa'
    teste2 = 'çplokiju'
    print(teste(teste1))

