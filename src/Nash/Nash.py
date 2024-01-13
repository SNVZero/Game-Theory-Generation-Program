import random

import numpy as np
import nashpy


class Nash:

    def __init__(self):
        self.A = []
        self.B = []
        self.a = []
        self.b = []
        self.Nash = []
        self.pareto = []
        self.answer = []

    def generate_game(self):
        for i in range(2):
            self.A.append(random.sample(range(21), 2))
            self.B.append(random.sample(range(21), 2))
        Flag = False
        self.A = np.array(self.A)
        self.B = np.array(self.B)
        row_max = np.argmax(self.A, axis=1)
        col_max = np.argmax(self.B, axis=0)
        # print(row_max)
        # print(col_max)
        if (row_max[0] == col_max[0] or row_max[1] == col_max[1]):
            Flag = True
        if (Flag == False):
            self.A, self.B = [], []
            self.generate_game()
        else:
            self.execute()

    def execute(self):
        for i in range(2):
            for j in range(2):
                is_pareto = True
                for k in range(2):
                    for l in range(2):
                        if self.A[k][l] > self.A[i][j] and self.B[k][l] > self.B[i][j]:
                            is_pareto = False
                if is_pareto:
                    self.pareto.append(f'A{i + 1}B{j + 1}')
        self.find_Nash()

    def find_Nash(self):
        # print(f"A = {self.A}")
        # print(" ")
        # print(f"B = {self.B}")
        game2 = nashpy.Game(self.A, self.B)
        # print(game2)
        equilibria = game2.support_enumeration()
        for eq in equilibria:
            # print(eq)
            if (eq[0][0] == 1):
                self.a.append(0)
            elif (eq[0][0] == 0):
                self.a.append(1)
            if (eq[1][0] == 1):
                self.b.append(0)
            elif (eq[1][0] == 0):
                self.b.append(1)
        for i in range(len(self.a)):
            # print(f"A{self.a[i] + 1}B{self.b[i] + 1}")
            self.Nash.append(f"A{self.a[i] + 1}B{self.b[i] + 1}")
            self.answer.append(f"({self.A[i][i]};{self.B[i][i]})")
        # print(f"Парето: {self.pareto}")
        # print(f"Нэш: {self.Nash}")


if __name__ == '__main__':
    play = Nash()
    play.generate_game()
