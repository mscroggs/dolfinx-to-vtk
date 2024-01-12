import pytest
import perms


def check_equal(a, b):
    print(a)
    print(b)
    assert len(a) == len(b)
    for i, j in zip(a, b):
        assert i == j


@pytest.mark.parametrize("degree", range(1, 9))
def test_tri(degree):
    target = [0, 1, 2]
    j = 3
    target += [2 * degree + k for k in range(1, degree)]
    target += [2 + k for k in range(1, degree)]
    target += [2 * degree + 1 - k for k in range(1, degree)]
    if degree == 3:
        target += [len(target) + i for i in [0]]
    elif degree == 4:
        target += [len(target) + i for i in [0, 1, 2]]
    elif degree == 5:
        target += [len(target) + i for i in [0, 2, 5, 1, 4, 3]]
    elif degree == 6:
        target += [len(target) + i for i in [0, 3, 9, 1, 2, 6, 8, 7, 4, 5]]
    elif degree == 7:
        target += [len(target) + i for i in [0, 4, 14, 1, 2, 3, 8, 11, 13, 12, 9, 5, 6, 7, 10]]
    elif degree == 8:
        target += [len(target) + i for i in [0, 5, 20, 1, 2, 3, 4, 10, 14, 17, 19,
                                             18, 15, 11, 6, 7, 9, 16, 8, 13, 12]]
    elif degree == 9:
        target += [len(target) + i for i in [0, 6, 27, 1, 2, 3, 4, 5, 12, 17, 21, 24, 26, 25,
                                             22, 18, 13, 7, 8, 11, 23, 9, 10, 16, 20, 19, 14, 15]]

    check_equal(perms.tri(degree), target)

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
        28, 29, 30, 23, 24, 22, 25, 27, 26, 31, 33, 32,
        34
    ])


@pytest.mark.parametrize("degree", range(5, 10))
def test_tet(degree):
    p = perms.tet(degree)
    assert len(p) == (degree + 1) * (degree + 2) * (degree + 3) // 6
    assert len(set(p)) == len(p)
