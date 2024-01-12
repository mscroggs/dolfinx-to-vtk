def hex(degree):
    p = []
    for v in [0, 1, 3, 2, 4, 5, 7, 6]:
        p += [v]
    base = 8
    if degree > 1:
        n = degree - 1
        for edge in [0, 3, 5, 1, 8, 10, 11, 9, 2, 4, 7, 6]:
            for i in range(n):
                p.append(base + n * edge + i)

        base += 12 * n

        n = (degree - 1) * (degree - 1)
        for face in [2, 3, 1, 4, 0, 5]:
            for i in range(n):
                p.append(base + n * face + i)
        base += 6 * n

        n = (degree - 1) * (degree - 1) * (degree - 1)
        for i in range(n):
            p.append(base + i)

    return p


def tet(degree):
    p = []
    for vertex in [0, 1, 2, 3]:
        p.append(vertex)

    base = 4
    if degree > 1:
        n = degree - 1
        for edge in [5, 2, 4, 3, 1, 0]:
            if edge == 4:
                for i in range(n):
                    p.append(base + n * edge + n - 1 - i)
            else:
                for i in range(n):
                    p.append(base + n * edge + i)

        base += 6 * n
    print(p)
    if degree > 2:
        n = (degree - 1) * (degree - 2) // 2
        for face in [2, 0, 1, 3]:
            for i in range(n):
                p.append(base + n * face + i)
        base += 4 * n
    if degree > 3:
        n = (degree - 1) * (degree - 2) * (degree - 3) // 6
        for i in range(n):
            p.append(base + i)

    return p
