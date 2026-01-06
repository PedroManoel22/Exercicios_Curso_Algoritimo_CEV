# 57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. 
# No final, mostre o total de salários pagos aos homens e o total pago às 
# mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não 
# sempre que ler os dados de um funcionário.

from ex_037 import valida_salario_atual, valida_sexo

if __name__ == '__main__':
    count = 1
    salario_homens = 0
    salario_mulheres = 0

    while True:
        print(f'\n---- Dados do(a) {count}° funcionário(a) ----\n')
        salario = valida_salario_atual()
        sexo = valida_sexo()

        if sexo == 'M':
            salario_homens += salario
        
        elif sexo == 'F':
            salario_mulheres += salario

        while True:
            continuar = input('Deseja continuar [S/N]? ').upper().strip()

            if continuar != 'S' and continuar != 'N':
                print('\n\033[1;31mPor favor insira uma opção válida!\033[m\n')
            
            else:
                count += 1
                break

        if continuar == 'N':
            print(f'\nTotal dos salários dos homens: {salario_homens}\n'
                  f'Total dos salários das mulheres: {salario_mulheres}\n')
            break
