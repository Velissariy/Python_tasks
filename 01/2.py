def sort_list_imperative(numbers):
    """
    Императивный стиль. Быстрая сортировка.
    :param numbers:
    :return:
    """
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [x for x in numbers[1:] if x >= pivot]
    right = [x for x in numbers[1:] if x < pivot]
    return sort_list_imperative(left) + [pivot] + sort_list_imperative(right)

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_list_imperative(numbers)
print("Отсортированный список:", sorted_numbers)