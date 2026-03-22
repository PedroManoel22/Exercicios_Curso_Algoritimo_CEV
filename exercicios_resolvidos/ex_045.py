# 45) O programa acima vai ter um problema quando digitarmos o primeiro valor
# maior que o último. Resolva esse problema com um código que funcione em qualquer
# situação.

from ex_044 import valida_valor_final, valida_valor_incremento, valida_valor_inicial


def fazer_contagem(inicio: int, fim: int, incremento: int):
    if inicio > fim:
        print(
            "\n\033[1;33mComo o inicio é maior que o fim, o incremento deve ser negativo, pode deixar comigo que já coloquei como negativo!\033[m\n"
        )
        incremento = -incremento

        print()
        for i in range(inicio, fim - 1, incremento):
            print(f"{i} ", end="")
    else:
        print()
        for i in range(inicio, fim + 1, incremento):
            print(f"{i} ", end="")

    print("Acabou!\n")


if __name__ == "__main__":
    inicio = valida_valor_inicial()
    fim = valida_valor_final()
    incremento = valida_valor_incremento()
    fazer_contagem(inicio, fim, incremento)
