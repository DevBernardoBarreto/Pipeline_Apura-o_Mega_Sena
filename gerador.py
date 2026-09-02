import csv
import random
import string


def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


def gerar_aposta():
    quantidade = random.randint(6, 15)
    numeros = sorted(random.sample(range(1, 61), quantidade))
    return numeros


def gerar_arquivo(nome_arquivo="apostas.csv", quantidade_linhas=10):
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        for _ in range(quantidade_linhas):
            identificador = gerar_id()
            numeros = gerar_aposta()

            escritor.writerow([identificador] + numeros)


if __name__ == "__main__":
    gerar_arquivo()

    print("Arquivo apostas.csv gerado com sucesso!")