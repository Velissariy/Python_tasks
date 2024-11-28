def sort_list_declarative(numbers):
    """
    Декларативный стиль. Встроенная фукнция sorted
    :param numbers:
    :return:
    """
    return sorted(numbers, reverse=True)

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный список:", sorted_numbers)