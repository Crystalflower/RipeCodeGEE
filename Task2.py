from math import sqrt

a = [
    {'x': 1, 'y': 1},
    {'x': 1, 'y': -1},
    {'x': -1, 'y': -2},
]
a_2 = [
    {'x': 1, 'y': 1},
    {'x': 1, 'y': -1},
    {'x': -1, 'y': -2},
    {'x': 2, 'y': 1},
    {'x': 2, 'y': 2},
    {'x': 3, 'y': -3}
]


def circle(coordinates):
    radius = set()  # у каждой окружности будет свой радиус, множество удалит дубликаты
    for i in range(len(coordinates)):  # перебор индексов элементов списка с координатами
        val = list(coordinates[i].values())  # извлекаем значения словаря по этому индексу и преобразуем их в список
        rad = sqrt(val[0] ** 2 + val[1] ** 2)  # вычисляем радиус как гипотенузу треугольника
        radius.add(rad)

    return f'Заданные точки лежат на {len(radius)} окружностях.'


print(circle(a))

print(circle(a_2))
