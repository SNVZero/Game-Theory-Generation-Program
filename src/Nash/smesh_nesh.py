import numpy as np


class smesh_nesh:
    def __init__(self, array1, array2, va, vb, sa, sb):
        self.A = array1
        self.B = array2
        self.SA = sa
        self.SB = sb
        self.VA = va
        self.VB = vb
        self.pareto = []

    def prin(self):
        print(self.A)
        print(self.B)
        print(self.SA)
        print(self.SB)
        print(self.VA)
        print(self.VB)

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


def initFunction():
    N = 2
    M = 2
    ok = 0
    while (ok == 0):
        mata = np.random.choice(np.arange(1, 99), size=(N, M), replace=False)
        matb = np.random.choice(np.arange(1, 99), size=(N, M), replace=False)
        maxa = np.array(mata.max(axis=0))
        maxb = np.array(matb.max(axis=1))
        coora1 = np.where(mata == maxa[0])
        cora1 = list(zip(coora1[0], coora1[1]))
        coora2 = np.where(mata == maxa[1])
        cora2 = list(zip(coora2[0], coora2[1]))
        coorb1 = np.where(matb == maxb[0])
        corb1 = list(zip(coorb1[0], coorb1[1]))
        coorb2 = np.where(matb == maxb[1])
        corb2 = list(zip(coorb2[0], coorb2[1]))
        if (cora1 != corb1) & (cora1 != corb2) & (cora2 != corb1) & (cora2 != corb2):
            ok = 1
    p = (matb[1][1] - matb[1][0]) / (matb[0][0] + matb[1][1] - matb[0][1] - matb[1][0])
    q = (mata[1][1] - mata[0][1]) / (mata[0][0] + mata[1][1] - mata[0][1] - mata[1][0])
    sa = np.array([p, (1 - p)])
    sb = np.array([q, (1 - q)])
    x = sa
    y = sb.transpose()
    va = np.dot(x, mata)
    va = np.dot(va, y)
    vb = np.dot(x, matb)
    vb = np.dot(vb, y)
    return smesh_nesh(mata, matb, va, vb, sa, sb)


# m = initFunction()
# # print("Nesh:")
# # m.prin()
# m.execute()
# print("pareto:")
# print(m.pareto)
