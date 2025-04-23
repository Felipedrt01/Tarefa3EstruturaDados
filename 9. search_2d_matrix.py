print("=== Buscar valor na matriz ===")

def search_2d_matrix(matrix, target):
    def recursive_search(matrix, target, row, col):
        if row >= len(matrix) or col < 0:
            return False
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            return recursive_search(matrix, target, row, col - 1)
        else:
            return recursive_search(matrix, target, row + 1, col)

row_len = int(input("Digite o número de linhas da matriz: "))
col_len = int(input("Digite o número de colunas da matriz: "))
matrix = []
for _ in range(row_len):
    row = list(map(int, input("Digite os elementos da linha separados por espaço: ").split()))
    matrix.append(row)

target = int(input("Digite o valor para buscar na matriz: "))
if search_2d_matrix(matrix, target):
    print("Valor encontrado!")
else:
    print("Valor não encontrado.")
