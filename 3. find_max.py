print("=== Procurar o maior número ===")

def find_max(arr):
    def body(arr, lo, hi):
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        left_max = body(arr, lo, mid)
        right_max = body(arr, mid + 1, hi)
        return left_max if left_max > right_max else right_max
    return body(arr, 0, len(arr) - 1)


def prob3():
    arr = list(map(int, input("Digite números aleatórios separados por espaço: ").split()))

    print("Estes são os números dos quais você digitou:", arr)
    print("O maior deles é o:", find_max(arr))
prob3()
