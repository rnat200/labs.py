from typing import List, Tuple

def find_last_min_element_index(arr: List[float]) -> Tuple[float, int]:
    if not arr:
        raise ValueError("Массив не должен быть пустым")

    min_value = arr[0]
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] <= min_value:
            min_value = arr[i]
            min_index = i

    return min_value, min_index

def sum_between_negatives(arr: List[int]) -> int:
    neg_indices = [idx for idx, val in enumerate(arr) if val < 0]
    if len(neg_indices) < 2:
        return 0
    first_neg = neg_indices[0]
    last_neg = neg_indices[-1]
    return sum(arr[first_neg + 1: last_neg])

arr = [3, -2, 8, 4, -5, 7, -1, 9]
min , index = find_last_min_element_index(arr)
print(f"Минимальный эл-т в массиве: {min} а индекс {index}")
print(f"Исходный массив: {arr}")

print(f"Сумма элементов между отриц = {sum_between_negatives(arr)}")