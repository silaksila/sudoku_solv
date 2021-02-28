import numpy as np


def check(y, x, n):
    global num

    for i in range(0, 9):
        if num[y][i] == n:
            return False
    for i in range(0, 9):
        if num[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if num[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global num, completed_board
    for y in range(9):
        for x in range(9):
            if num[y][x] == 0:
                for n in range(1, 10):
                    if check(y, x, n):
                        num[y][x] = n
                        solve()
                        num[y][x] = 0
                return
    ###########################################################################################
    array = np.array(num)
    with open('solved.txt', 'wb')as f:
        np.save(f, array)

    with open('solved.txt', 'rb') as f:
        completed_board = np.load(f).tolist()
