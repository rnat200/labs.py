import numpy as np

def solve_variant_4(matrix: np.ndarray)-> None:
    has_zero_mask = np.any(matrix == 0, axis=0)
    col_sums = matrix.sum(axis=0)
    zero_sums = col_sums[has_zero_mask]

    sort_matrix = matrix.copy()
    sort_matrix[::2, :] = np.sort(sort_matrix[::2, :], axis=1)
    sort_matrix[1::2, :] = np.sort(sort_matrix[1::2, :], axis=1)[:, ::-1]

    print(f"Сумма столбцов с нулями = {zero_sums}")

    print("Отсортированная матрица (четные строки по возрастанию нечет по убыванию)")
    print (sort_matrix)

matrix = np.random.randint(-3, 4, size=(4, 5))
print("Исходная матрица:")
print(matrix)
solve_variant_4(matrix)