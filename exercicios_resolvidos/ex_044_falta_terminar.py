# 44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o 
# incremento, mostrando em seguida todos os valores no intervalo: 
# Ex: Digite o primeiro Valor: 3 
# Digite o último Valor: 10 
# Digite o incremento: 2 
# Contagem: 3 5 7 9 Acabou! 

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