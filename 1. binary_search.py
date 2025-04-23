print("=== Busca Binária ===")

def binary_search():
    numeros = list(map(int, input("Digite números aleatórios separados por espaço: ").split()))
    numeros.sort()
    print(f"Lista ordenada: {numeros}")

    alvo = int(input("Digite o número que deseja buscar: "))

    esquerda, direita = 0, len(numeros) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if numeros[meio] == alvo:
            print(f"Número {alvo} encontrado na posição {meio} da lista ordenada.")
            return
        elif numeros[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    print(f"Número {alvo} não encontrado na lista.")


if __name__ == "__main__":
    binary_search()
