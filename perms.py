import math


def int_sqrt(n):
    return int(math.floor(math.sqrt(n)))


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


def tri(degree):
    num_nodes = (degree + 1) * (degree + 2) // 2
    out = [0, 1, 2]
    if degree == 1:
        return out
    base = 3
    n = degree - 1
    for edge in [2, 0, 1]:
        if edge == 1:
            for i in range(n):
                out.append(base + edge * n + n - 1 - i)
        else:
            for i in range(n):
                out.append(base + edge * n + i)
    base += 3 * n

    if base < num_nodes:
        remainders = list(range(num_nodes - base))

        out += [base + i for i in tri_remainders(remainders)]

    return out


def tri_remainders(remainders):
    out = []
    while len(remainders) > 0:
        if len(remainders) == 1:
            out.append(remainders[0])
            remainders = []
            break

        deg = (int_sqrt(1 + 8 * len(remainders)) - 1) // 2 - 1

        out.append(remainders[0])
        remainders = remainders[1:]
        out.append(remainders[deg - 1])
        remainders = remainders[:deg - 1] + remainders[deg:]
        out.append(remainders[-1])
        remainders = remainders[:-1]

        for _ in range(deg - 1):
            out.append(remainders[0])
            remainders = remainders[1:]

        k = deg * (deg - 1) // 2
        for i in range(deg - 1):
            out.append(remainders[-k])
            if k == 1:
                remainders = remainders[:-k]
            else:
                remainders = remainders[:-k] + remainders[-k+1:]
            k -= deg - i - 1

        k = 1
        for i in range(deg - 1):
            out.append(remainders[-k])
            if k == 1:
                remainders = remainders[:-k]
            else:
                remainders = remainders[:-k] + remainders[-k+1:]
            k += i + 1

    return out


def tet(degree):
    p = []
    for vertex in [0, 1, 2, 3]:
        p.append(vertex)

    if degree == 1:
        return p

    base = 4
    n = degree - 1
    for edge in [5, 2, 4, 3, 1, 0]:
        if edge == 4:
            for i in range(n):
                p.append(base + n * edge + n - 1 - i)
        else:
            for i in range(n):
                p.append(base + n * edge + i)

    base += 6 * n

    if degree <= 2:
        return p

    n = (degree - 1) * (degree - 2) // 2
    face_order = tri(n)
    for face in [2, 0, 1, 3]:
        face_dofs = []
        if face == 2:
            for i in range(n):
                face_dofs.append(base + n * face + i)
        elif face == 0:
            # rot1
            face_dofs = []
            for i in range(degree - 3, -1, -1):
                d = i
                for j in range(i + 1):
                    face_dofs.append(base + n * face + d)
                    d += degree - 3 - j
        else:
            # ref1
            for i in range(degree - 2):
                d = i
                for j in range(degree - 2 - i):
                    face_dofs.append(base + n * face + d)
                    d += degree - 2 - j
        p += tri_remainders(face_dofs)
    base += 4 * n

    if degree <= 3:
        return p

    n = (degree - 1) * (degree - 2) * (degree - 3) // 6
    remainders = [base + i for i in range(n)]

    p += tet_remainders(remainders)
    return p


def tet_remainders(remainders):
    out = []
    while len(remainders) > 0:
        if len(remainders) == 1:
            out.append(remainders[0])
            remainders = []
            break

        deg = 0
        while deg * (deg + 1) * (deg + 2) < 6 * len(remainders):
            deg += 1

        for dof in [0, deg - 2, deg * (deg + 1) // 2 - 3, -1]:
            out.append(remainders[dof])
            if dof + 1 in [0, len(remainders)]:
                remainders = remainders[:dof]
            else:
                remainders = remainders[:dof] + remainders[dof + 1:]

        if deg > 2:
            for i in range(deg - 2):
                out.append(remainders[0])
                remainders = remainders[1:]
            d = deg - 2
            for i in range(deg - 2):
                out.append(remainders[d])
                remainders = remainders[:d] + remainders[d + 1:]
                d += deg - 3 - i
            d = deg * (deg - 3) // 2
            for i in range(deg - 2):
                out.append(remainders[d])
                remainders = remainders[:d] + remainders[d + 1:]
                d -= deg - 3 - i
            d = (deg - 3) * (deg - 2) // 2
            for i in range(deg - 2):
                out.append(remainders[d])
                remainders = remainders[:d] + remainders[d + 1:]
                d += (deg - i) * (deg - i - 1) // 2  - 1
            d = (deg - 3) * (deg - 2) // 2 + deg - 3
            for i in range(deg - 2):
                out.append(remainders[d])
                remainders = remainders[:d] + remainders[d + 1:]
                d += (deg - 2 - i) * (deg - 1 - i) // 2 + deg - 4 - i
            d = (deg - 3) * (deg - 2) // 2 + deg - 3 + (deg - 2) * (deg - 1) // 2 - 1
            for i in range(deg - 2):
                out.append(remainders[d])
                remainders = remainders[:d] + remainders[d + 1:]
                d += (deg - 3 - i) * (deg - 2 - i) // 2 + deg - i - 5

        if deg > 3:
            dofs = []
            d = (deg - 3) * (deg - 2) // 2
            for i in range(deg - 3):
                for j in range(deg - 3 - i):
                    print(d)
                    dofs.append(remainders[d])
                    d += 1
                d += (deg - 2 - i) * (deg - 1 - i) // 2

            print(dofs)
            remainders += tri_remainders(dofs)

            # TODO

            print(deg, "r", len(remainders))
        print()

    return out
