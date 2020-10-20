a = [5, 1, 3, 6, 8, -2, 8, -1, 1, 18]
rev_a = a[::-1]
n = 10
m = 3
sum_m = 0


def calculate(list):
    global sum_m
    for i in range(0, len(list), m):
        if i <= len(list) - m:
            new = []
            for j in range(m):
                new.append(list[i + j])
            if sum(new) > sum_m:
                sum_m = sum(new)


calculate(a)
calculate(rev_a)
print(sum_m)
