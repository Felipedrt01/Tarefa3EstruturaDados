print("=== Procurar o menor número ===")

def find_min(arr):
    def body(arr, lo, hi):
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        left_min = body(arr, lo, mid)
        right_min = body(arr, mid + 1, hi)
        return left_min if left_min < right_min else right_min

    return body(arr, 0, len(arr) - 1)


def prob4():
    arr = list(map(int, input("Digite números aleatórios separados por espaço: ").split()))

    print("Estes são os números dos quais você digitou:", arr)
    print("O menor deles é o:", find_min(arr))


prob4()
