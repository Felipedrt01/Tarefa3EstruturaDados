print("=== Somar números ===")

def find_sum(arr):
    def body(arr, lo, hi):
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        left_sum = body(arr, lo, mid)
        right_sum = body(arr, mid + 1, hi)
        return left_sum + right_sum
    return body(arr, 0, len(arr) - 1)

def prob5():
    arr = list(map(int, input("Digite números aleatórios separados por espaço: ").split()))
    print("Somando eles, o resultado é:", find_sum(arr))

prob5()
