def hex(degree):
    dof_n = 0

    dofs_on_entities = [[], [], [], []]
    for vertex in range(8):
        dofs_on_entities[0].append([dof_n])
        dof_n += 1
    for edge in range(12):
        dofs = []
        for i in range(degree - 1):
            dofs.append(dof_n)
            dof_n += 1
        dofs_on_entities[1].append(dofs)
    for face in range(6):
        dofs = []
        for i in range((degree - 1) ** 2):
            dofs.append(dof_n)
            dof_n += 1
        dofs_on_entities[2].append(dofs)
    dofs = []
    for i in range((degree - 1) ** 3):
        dofs.append(dof_n)
        dof_n += 1
    dofs_on_entities[3].append(dofs)

    p = []
    for v in [0, 1, 3, 2, 4, 5, 7, 6]:
        p += dofs_on_entities[0][v]
    if degree > 1:
        #for edge, reverse in [
        #    (0, False), (3, True), (11, False), (1, False), (8, False), (2, False),
        #    (10, False), (9, False), (4, False), (7, True), (5, False), (6, False),
        #]:
        for edge, reverse in [
            (0, False), (3, False), (5, False), (1, True), (8, False), (10, False),
            (11, False), (9, True), (2, False), (4, False), (7, False), (6, False),
        ]:
            if reverse:
                p += dofs_on_entities[1][edge][::-1]
            else:
                p += dofs_on_entities[1][edge]

        for face in [2, 3, 1, 4, 0, 5]:
            p += dofs_on_entities[2][face]

        p += dofs_on_entities[3][0]

    print(p)

    return p

