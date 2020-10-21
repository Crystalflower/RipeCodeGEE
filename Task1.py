a = [5, 1, 3, 6, 8, -2, 8, -1, 1, 18]

m = 3
n = 10

a_2 = [1, 8, 9, 9, 9, 3, -5, 4]

step = 4
l = 8


def calculate(sequence, param_1, param_2):
    new_sequence = [sequence[i] for i in range(param_1)]  # генерируем список из m-элементов исходного
    sum_s = sum(new_sequence)  # введем параметр суммы и сразу ее посчитаем
    for i in range(param_1, param_2):  # перебираем оставшиеся элементы, для второго параметра также подойдет len(a)
        del new_sequence[0]  # удаляем первый элемент новой последовательности
        new_sequence.append(sequence[i])  # вставляем в конец следующий элемент начальной последовательности
        if sum(new_sequence) > sum_s:
            sum_s = sum(new_sequence)  # сравниваем сумму m-элементов и обновляем при большем значении
    return sum_s


print(calculate(a, m, n))

print(calculate(a_2, step, l))
