print("=== Encontrar posição em uma lista onde um valor pode ser inserido mantendo a ordem. ===")

from bisect import bisect_left, bisect_right
def bisect_right_left(arr, target):
    left = bisect_left(arr, target)
    right = bisect_right(arr, target)
    print(f"Posição para inserir à esquerda: {left}")
    print(f"Posição para inserir à direita: {right}")

def prob7():
    arr = list(map(int, input("Digite números aleatórios separados por espaço, (ordenados): ").split()))
    target = int(input("Escolha um valor: "))
    bisect_right_left(arr, target)

prob7()
