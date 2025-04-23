print("=== Procura de posição ===")

def search_position(arr, target):
    def body(arr, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return body(arr, target, mid + 1, high)
        else:
            return body(arr, target, low, mid - 1)
    return body(arr, target, 0, len(arr) - 1)

def prob6():
    arr = list(map(int, input("Digite números aleatórios separados por espaço (em ordem crescente): ").split()))
    target = int(input("Digite o valor para buscar: "))
    result = search_position(arr, target)
    if result >= 0:
        print(f"Posição do valor {target}: {result}")
    else:
        print(f"Valor {target} não encontrado.")

prob6()
