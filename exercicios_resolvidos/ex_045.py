# 45) O programa acima vai ter um problema quando digitarmos o primeiro valor 
# maior que o último. Resolva esse problema com um código que funcione em qualquer 
# situação. 


def valida_valor_inicial():
    print()
    while True:
        try:
            valor = int(input('Digite o primeiro valor: '))
            return valor
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
        
        except Exception as e:
            print(f'\n\033[1;31mErro inesperado!, {e.__class__.__name__}\033[m\n')
        

def valida_valor_final():
    print()
    while True:
        try:
            valor = int(input('Digite o último valor: '))
            return valor
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
        
        except Exception as e:
            print(f'\n\033[1;31mErro inesperado!, {e.__class__.__name__}\033[m\n')
        

def valida_valor_incremento():
    print()
    while True:
        try:
            valor = int(input('Digite o incremento: '))
            return valor
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número inteiro!\033[m\n')
        
        except Exception as e:
            print(f'\n\033[1;31mErro inesperado!, {e.__class__.__name__}\033[m\n')


def fazer_contagem(inicio, fim, incremento):
    if inicio > fim:
        print('\n\033[1;33mComo o inicio é maior que o fim, o incremento deve ser negativo, pode deixar comigo que já coloquei como negativo!\033[m\n')
        incremento = -incremento

        print()
        for i in range(inicio, fim - 1, incremento):
            print(f'{i} ', end='')
    else:
        print()
        for i in range(inicio, fim + 1, incremento):
                print(f'{i} ', end='')
        
    print('Acabou!\n')


if __name__ == '__main__':
    inicio = valida_valor_inicial()
    fim = valida_valor_final()
    incremento = valida_valor_incremento()
    fazer_contagem(inicio, fim, incremento)