list_a = [0, 1, 2, 3, 4, 5, 6]
list_b = [8, 9, 10, 11, 76, 23]
list_c = []


def zwrot(a, b):
    for i in range(len(list_a)):
        if i % 2 == 0:
            list_c.append(list_a[i])
        else:
            list_c.append(list_b[i])


zwrot(list_a, list_b)
print(list_c)
