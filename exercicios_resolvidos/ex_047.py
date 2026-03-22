# 47) Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 +
# 450 + 400 + 350 + 300 + ... + 50 + 0

from ex_046 import mostrar_dados, somar

if __name__ == "__main__":
    INTERVALO = [x for x in range(500, -1, -50)]
    soma = somar(INTERVALO)
    mostrar_dados(INTERVALO, soma)
