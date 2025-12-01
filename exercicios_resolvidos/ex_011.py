# 11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do 
# segundo grau e mostre o valor de Delta.

def valida_A():
    while True:
        try:
            a = float(input('Digite o valor de a: '))
            if a == 0:
                print('\n\033[1;31mO coeficiente a não pode ser igual a 0\033[m\n')

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número válido!\n\033[m')
    
    return a


def valida_B():
    while True:
        try:
            b = float(input('Digite o valor de b: '))
            break

        except ValueError:
            print('\n\033[1;31mPor favor coloque um número válido!\n\033[m')
        
    return b
        
    
def valida_C():
    while True:
        try:
            c = float(input('Digite o valor de c: '))
            break
    
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número válido!\n\033[m')
    
    return c
    

def calcula_delta(a, b, c):
    if b == 0 or c == 0:
        print('\n\033[1;31mA equação está incompleta!\033[m')
    else:
        delta = (b ** 2) - 4 * a * c
        return delta


if __name__ == '__main__':
    a = valida_A()
    b = valida_B()
    c = valida_C()
    delta = calcula_delta(a, b, c)
    if delta:
        print(f'\nO delta da função é {delta}')
    