# 61) Crie um programa que mostre na tela a seguinte contagem, usando a estrutura 
# “faça enquanto” 
# 0 3 6 9 12 15 18 21 24 27 30 Acabou! 
count = 0
print()
while count <= 30:
    print(f'{count} ', end='')
    count += 3
print('Acabou!\n')