import csv
import random
import string
import sys


def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


def gerar_aposta():
    quantidade = random.randint(1, 20)
    numeros = sorted(random.sample(range(1, 61), quantidade))
    return numeros


def validar_aposta(numeros):
    return 6 <= len(numeros) <= 15


def gerar_arquivo(nome_arquivo, quantidade_linhas):
    linhas_geradas = 0

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        while linhas_geradas < quantidade_linhas:
            identificador = gerar_id()
            numeros = gerar_aposta()

            if validar_aposta(numeros):
                escritor.writerow([identificador] + numeros)
                linhas_geradas += 1


def main():
    if len(sys.argv) != 2:
        print("Uso: python gerador.py <quantidade_de_linhas>")
        sys.exit(1)

    try:
        quantidade_linhas = int(sys.argv[1])
    except ValueError:
        print("Erro: a quantidade de linhas deve ser um número inteiro.")
        sys.exit(1)

    if quantidade_linhas <= 0:
        print("Erro: a quantidade de linhas deve ser maior que zero.")
        sys.exit(1)

    gerar_arquivo("apostas.csv", quantidade_linhas)

    print(f"Arquivo apostas.csv gerado com {quantidade_linhas} linhas válidas!")


if __name__ == "__main__":
    main()