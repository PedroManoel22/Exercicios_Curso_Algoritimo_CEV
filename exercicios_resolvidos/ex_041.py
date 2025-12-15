# 41) Desenvolva um programa que mostre na tela a seguinte contagem: 
# 100 95 90 85 80 ... 0 Acabou! 

nums = [x for x in range(100, -1, -5)]

print()
for num in nums:
    print(f'{num} ', end='')

print('Acabou!\n')