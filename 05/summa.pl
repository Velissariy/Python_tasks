sum_list([], 0).
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.


# sum_list([], 0).
# sum_list([Head|Tail], Sum) :-
#     integer(Head),  % Проверка, что элемент - целое число
#     sum_list(Tail, TailSum),
#     Sum is Head + TailSum,
#     !.
# sum_list([_|Tail], Sum) :-  % Обработка нечисловых элементов
#     sum_list(Tail, Sum),
#  !.
# sum_list(X, 0) :-
#     \+ is_list(X),
#     write('Ошибка: Входной параметр должен быть списком.'),
#     !.


