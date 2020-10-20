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
    {'x': 3, 'y': -3}
]


def circle(list):
    m_max = 0
    count = 0
    for i in range(len(list)):
        for j in list[i]:
            if abs(list[i].get(j)) > m_max:
                m_max += 1
                count += 1
    return f'Заданные точки принадлежат к {count} окружностям.'


print(circle(a))

print(circle(a_2))
