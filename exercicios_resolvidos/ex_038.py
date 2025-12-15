# 38) Escreva um programa que mostre na tela a seguinte contagem:  
# 6 7 8 9 10 11 Acabou! 
nums = [x for x in range(6, 12)]

print()
for num in nums:
    print(f'{num} ', end='')

print('Acabou!\n')