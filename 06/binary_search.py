def binary_search(arr, target):
    """
    Реализует бинарный поиск в отсортированном массиве.

    Args:
        arr: Отсортированный целочисленный массив.
        target: Целочисленное значение, которое нужно найти.

    Returns:
        Индекс элемента, если он найден, иначе -1.
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Целочисленное деление

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# sorted_array = [2, 5, 7, 8, 11, 12]
# target_value = 11

# result = binary_search(sorted_array, target_value)

# if result != -1:
#     print(f"Элемент {target_value} найден по индексу: {result}")
# else:
#     print(f"Элемент {target_value} не найден в массиве.")