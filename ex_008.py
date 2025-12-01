# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores 
# relativos em outras medidas. 
# Ex:  
# Digite uma distância em metros: 185.72 
# A distância de 185.7m corresponde a: 
# 0.18572Km 
# 1.8572Hm 
# 18.572Dam 
# 1857.2dm 
# 18572.0cm 
# 185720.0mm 

def valida_distancia():
    while True:
        try:
            distancia = float(input('Digite uma distância em metros: '))
            break
        
        except ValueError:
            print('\n\033[1;31mPor favor coloque um número real!\n\033[m')
    
    return distancia


def converter_distancia(distancia):
    print(f'{distancia / 1000}Km\n'
          f'{distancia / 100}Hm\n'
          f'{distancia / 10}Dam\n'
          f'{distancia * 10}dm\n'
          f'{distancia * 100}cm\n'
          f'{distancia * 1000}mm')


if __name__ == '__main__':
    distancia = valida_distancia()
    converter_distancia(distancia)