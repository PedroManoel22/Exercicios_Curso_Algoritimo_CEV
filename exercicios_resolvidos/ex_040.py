# 40) Crie um aplicativo que mostre na tela a seguinte contagem: 
# 0 3 6 9 12 15 18 Acabou! 

nums = [x for x in range(0, 19) if x % 3 == 0 ]

print()
for num in nums:
    print(f'{num} ', end='')

print('Acabou!\n')