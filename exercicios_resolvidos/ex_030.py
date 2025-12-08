# 30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo 
# de triângulo será formado:  - EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois lados iguais - ESCALENO: todos os lados diferentes 

def valida_primeiro_segmento():
    while True:
        try:
            segmento1 = float(input('Insira o valor do primeiro segmento: '))
            
            if segmento1 <= 0:
                print('\n\033[1;35mNão é possível colocar um segmento de valor igual a 0 ou negativo!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um valor válido!\033[m\n')
    
    return segmento1


def valida_segundo_segmento():
    while True:
        try:
            segmento2 = float(input('Insira o valor do segundo segmento: '))
            
            if segmento2 <= 0:
                print('\n\033[1;35mNão é possível colocar um segmento de valor igual a 0 ou negativo!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um valor válido!\033[m\n')
    
    return segmento2


def valida_terceiro_segmento():
    while True:
        try:
            segmento3 = float(input('Insira o valor do terceiro segmento: '))
            
            if segmento3 <= 0:
                print('\n\033[1;35mNão é possível colocar um segmento de valor igual a 0 ou negativo!\033[m\n')
                continue

            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um valor válido!\033[m\n')
    
    return segmento3


def forma_triangulo(seg1, seg2, seg3):
    regras = 0
    if seg1 < seg2 + seg3:
        regras += 1
    
        if seg2 < seg1 + seg3:
            regras += 1
    
            if seg3 < seg1 + seg2:
                regras += 1
    
    if regras == 3:
        return True
    
    else:
        return False


def tipo_triangulo(seg1, seg2, seg3):
    if seg1 == seg2 and seg2 == seg3 and seg3 == seg1:
        tipo = 'Equilátero'
    
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        tipo = 'Isósceles'
    
    else:
        tipo = 'Escaleno'
    
    return tipo
    

def exibir_dados(seg1, seg2, seg3, e_triangulo, tipo=0):
    if tipo == 0:
        if e_triangulo:
            resposta = '\033[1;32mSim\033[m'

        else:
            resposta = '\033[1;31mNão\033[m'

        print(f'\n1° segmento de reta = {seg1}\n'
            f'2° segmento de reta = {seg2}\n'
            f'3° segmento de reta = {seg3}\n'
            f'Forma um Triângulo ? {resposta}\n')
    
    else:
        if e_triangulo:
            resposta = '\033[1;32mSim\033[m'

        else:
            resposta = '\033[1;31mNão\033[m'

        print(f'\n1° segmento de reta = {seg1}\n'
            f'2° segmento de reta = {seg2}\n'
            f'3° segmento de reta = {seg3}\n'
            f'Forma um Triângulo ? {resposta}\n'
            f'Tipo do triângulo: {tipo}\n')


if __name__ == '__main__':
    segmento1 = valida_primeiro_segmento()
    segmento2 = valida_segundo_segmento()
    segmento3 = valida_terceiro_segmento()
    e_triangulo = forma_triangulo(segmento1, segmento2, segmento3)

    if e_triangulo:
        tipo = tipo_triangulo(segmento1, segmento2, segmento3)
        exibir_dados(segmento1, segmento2, segmento3, e_triangulo, tipo)

    else:
        exibir_dados(segmento1, segmento2, segmento3, e_triangulo)