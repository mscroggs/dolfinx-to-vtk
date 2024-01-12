import perms


def check_equal(a, b):
    assert len(a) == len(b)
    for i, j in zip(a, b):
        print(i, j)
        assert i == j


def test_hex_degree_1():
    check_equal(perms.hex(1), [0, 1, 3, 2, 4, 5, 7, 6])


def test_hex_degree_2():
    check_equal(perms.hex(2), [
        0, 1, 3, 2, 4, 5, 7, 6, 8, 11, 13, 9, 16, 18,
        19, 17, 10, 12, 15, 14, 22, 23, 21, 24, 20, 25, 26
    ])


def test_hex_degree_3():
    check_equal(perms.hex(3), [
        0, 1, 3, 2, 4, 5, 7, 6,
        8, 9, 14, 15, 18, 19, 10, 11, 24, 25, 28, 29, 30, 31, 26, 27, 12, 13, 16, 17, 22, 23, 20, 21,
        40, 41, 42, 43, 44, 45, 46, 47, 36, 37, 38, 39, 48, 49, 50, 51, 32, 33, 34, 35, 52, 53, 54, 55,
        56, 57, 58, 59, 60, 61, 62, 63
    ])


def test_tet_degree_1():
    check_equal(perms.tet(1), [0, 1, 2, 3])


def test_tet_degree_2():
    check_equal(perms.tet(2), [0, 1, 2, 3, 9, 6, 8, 7, 5, 4])


def test_tet_degree_3():
    check_equal(perms.tet(3), [0, 1, 2, 3, 14, 15, 8, 9, 13, 12,
                               10, 11, 6, 7, 4, 5, 18, 16, 17, 19])

def test_tet_degree_4():
    check_equal(perms.tet(4), [
        0, 1, 2, 3,
        19, 20, 21, 10, 11, 12, 18, 17, 16, 13, 14, 15, 7, 8, 9, 4, 5, 6,
        28, 29, 30, 22, 23, 24, 25, 26, 27, 31, 32, 33,
        34
    ])

def test_tet_degree_5():
    assert len(perms.tet(5)) == 7*8

def test_tet_degree_6():
    assert len(perms.tet(6)) == 7*8*9//6
