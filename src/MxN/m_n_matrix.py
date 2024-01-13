import numpy as np
from scipy.optimize import linprog


class Matrix_mxn:

    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.va = 0
        self.vb = 0
        self.p = []
        self.q = []

    def execute(self):
        # self.print()

        obj = [1] * self.m
        lhs_ineq = -1 * self.matrix.transpose()  # левая сторона неравенств
        rhs_ineq = [-1] * self.n  # правая сторона неравенств
        opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="highs")
        self.va = 1 / opt.fun  # цена игры
        self.va = round(self.va, 4)
        self.p = opt.x * self.va  # стратегия игрока A

        for obt in range(len(self.p)):
            self.p[obt] = round(self.p[obt], 4)

        obj = [-1] * self.n
        lhs_ineq = self.matrix  # левая сторона неравенств
        rhs_ineq = [1] * self.m  # правая сторона неравенств
        opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="highs")
        self.vb = -self.va
        self.q = opt.x * self.va  # стратегия игрока B

        for obt in range(len(self.q)):
            self.q[obt] = round(self.q[obt], 4)

    def print(self):
        print(self.matrix)


def init(m,n):
    while True:
        array = np.random.randint(0, 1000, (m, n))
        min_in_rows = np.min(array, axis=1)
        a = max(min_in_rows)
        # print(a)
        max_in_columns = np.max(array, axis=0)
        b = min(max_in_columns)
        # print(b)
        if a != b:
            break
    return array


if __name__ == '__main__':
    m = 4
    n = 6
    # while True:
    #     matrix = np.random.randint(0, 1000, (m, n))
    #     min_in_rows = np.min(matrix, axis=1)
    #     a = max(min_in_rows)
    #     print(a)
    #     max_in_columns = np.max(matrix, axis=0)
    #     b = min(max_in_columns)
    #     print(b)
    #     if a != b:
    #         break
    matrix = init(4,6)
    play = Matrix_mxn(matrix)
    play.execute()
    # print(play.va, play.vb,play.p, play.q)
