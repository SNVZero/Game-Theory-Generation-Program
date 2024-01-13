import random
import numpy as np


class n2_2m:
    def __init__(self, array, v, s1, s2):
        self.array = array
        self.S1 = s1
        self.S2 = s2
        self.V = v

    def prin(self):
        print(self.array)
        print(self.S1)
        print(self.S2)
        print(self.V)
        print(" ")


def initFunc():
    for orientetion in range(2):
        if orientetion == 0:
            N = 2
            M = 4
        else:
            N = 4
            M = 2
        vert = 0
        matrix = np.random.choice(np.arange(1, 20), size=(N, M), replace=False)
        if N > M:
            vert = 1
        a = max(matrix.min(axis=1))
        b = min(matrix.max(axis=0))
        if (N != 2) | (M != 2):
            while a == b:
                coor = np.where(matrix == a)
                cor = list(zip(coor[0], coor[1]))
                if vert == 0:
                    ind = cor[0][0] ^ 1
                    dom = 1
                    for i in range(M):
                        if matrix[cor[0][0]][i] < matrix[ind][i]:
                            dom = 0
                if vert == 1:
                    ind = cor[0][1] ^ 1
                    dom = 0
                    for i in range(N):
                        if matrix[i][cor[0][1]] > matrix[i][ind]:
                            dom = 1
                if dom == 0:
                    matrix[cor[0][0]][cor[0][1]] += 20
                    a = max(matrix.min(axis=1))
                    b = min(matrix.max(axis=0))
                else:
                    matrix[cor[0][0]][cor[0][1]] = 0
                    a = max(matrix.min(axis=1))
                    b = min(matrix.max(axis=0))
            mat = np.array(matrix)
            if vert == 1:
                matrix = np.array(np.transpose(matrix))
                M = N
                N = 2
                ed = np.eye(M)
                ed *= (-1)
                matrix = np.dot(matrix, ed)
            f = matrix[0].min()
            coor = np.where(matrix == f)
            cor = list(zip(coor[0], coor[1]))
            ar = np.array([[matrix[0][cor[0][1]], matrix[1][cor[0][1]]], ])
            matr = np.array(matrix)
            matrix = np.delete(matrix, cor[0][1], axis=1)
            for i in range(M - 1):
                n = 0
                l = 0
                while (n < len(ar)):
                    if ((matrix[0][i] > ar[n][0]) & (matrix[1][i] < ar[n][1])) | (
                            (matrix[0][i] < ar[n][0]) & (matrix[1][i] > ar[n][1])):
                        l = 1
                    if (matrix[0][i] <= ar[n][0]) & (matrix[1][i] <= ar[n][1]):
                        ar = np.vstack([ar, [matrix[0][i], matrix[1][i]]])
                        ar = np.delete(ar, n, axis=0)
                        l = 0
                    if (matrix[0][i] >= ar[n][0]) & (matrix[1][i] >= ar[n][1]):
                        l = 0
                        break
                    n += 1
                if l == 1:
                    ar = np.vstack([ar, [matrix[0][i], matrix[1][i]]])
            end = 0
            ar1 = np.array(ar.transpose())
            ar1 = ar1[:, ar1[0].argsort()]
            ar = ar1.transpose()
            x = 2
            y = -100
            a1 = 0
            a2 = 0
            c1 = 0
            c2 = 0
            for i in range(len(ar) - 1):
                for j in range(i + 1, len(ar)):
                    x1 = (ar[j][0] - ar[i][0]) / (ar[i][1] - ar[i][0] - (ar[j][1] - ar[j][0]))
                    y1 = (ar[i][1] - ar[i][0]) * x1 + ar[i][0]
                    ok = 0
                    if vert == 0:
                        if (x1 < 0) | (x1 > 1) | (y1 < 0):
                            continue
                    else:
                        if (x1 < 0) | (x1 > 1):
                            continue
                    for k in range(len(ar)):
                        if (ar[k][0] == ar[i][0]) | (ar[k][0] == ar[j][0]):
                            continue
                        if (y1 > ((ar[k][1] - ar[k][0]) * x1 + ar[k][0] + 0.0000000001)):
                            ok = 1
                            break
                        if (abs(y1 - ((ar[k][1] - ar[k][0]) * x1 + ar[k][0])) < 0.000000001):
                            for l in range(k + 1, len(ar)):
                                if (ar[l][0] == ar[i][0]) | (ar[l][0] == ar[j][0]):
                                    continue
                                if (y1 > ((ar[l][1] - ar[l][0]) * x1 + ar[l][0] + 0.0000000001)):
                                    ok = 1
                                    break
                            if ok == 1:
                                break
                            ok = 1
                            if (y1 >= y):
                                if ar[i][0] < ar[j][0]:
                                    if ar[i][0] < ar[k][0]:
                                        a1 = ar[i][0]
                                        a2 = ar[i][1]
                                    else:
                                        a1 = ar[k][0]
                                        a2 = ar[k][1]
                                else:
                                    if ar[j][0] < ar[k][0]:
                                        a1 = ar[j][0]
                                        a2 = ar[j][1]
                                    else:
                                        a1 = ar[k][0]
                                        a2 = ar[k][1]
                                if ar[i][1] < ar[j][1]:
                                    if ar[i][1] < ar[k][1]:
                                        c1 = ar[i][0]
                                        c2 = ar[i][1]
                                    else:
                                        c1 = ar[k][0]
                                        c2 = ar[k][1]
                                else:
                                    if ar[j][1] < ar[k][1]:
                                        c1 = ar[j][0]
                                        c2 = ar[j][1]
                                    else:
                                        c1 = ar[k][0]
                                        c2 = ar[k][1]
                                y = y1
                                x = x1
                            break
                    if ok == 0:
                        if y1 > y:
                            y = y1
                            x = x1
                            c1 = ar[j][0]
                            c2 = ar[j][1]
                            a1 = ar[i][0]
                            a2 = ar[i][1]
            if vert == 0:
                v = y
                p2 = x
                p1 = 1 - x
                coor1 = np.where(matr == c1)
                cor1 = list(zip(coor1[0], coor1[1]))
                coor2 = np.where(matr == a1)
                cor2 = list(zip(coor2[0], coor2[1]))
                aa = 0
                bb = 0
                if (cor2[0][1] < cor1[0][1]):
                    aa = a1
                    a1 = c1
                    c1 = aa
                    bb = c2
                    c2 = a2
                    a2 = bb
                q2 = (c1 - c2) / (c1 + a2 - c2 - a1)
                q1 = 1 - q2
                s2 = []
                for i in range(M):
                    if (i != cor1[0][1]) & (i != cor2[0][1]):
                        s2.append(0)
                    if (i == cor1[0][1]):
                        s2.append(q1)
                    if (i == cor2[0][1]):
                        s2.append(q2)
                s1 = [p1, p2]
                return n2_2m(mat, v, s1, s2)
                #m.prin()
            else:
                v = -y
                p2 = x
                p1 = 1 - p2
                coor1 = np.where(matr == c1)
                cor1 = list(zip(coor1[0], coor1[1]))
                coor2 = np.where(matr == a1)
                cor2 = list(zip(coor2[0], coor2[1]))
                if (cor2[0][1] < cor1[0][1]):
                    aa = a1
                    a1 = c1
                    c1 = aa
                    bb = c2
                    c2 = a2
                    a2 = bb
                q2 = (-c1 + c2) / (-c1 - a2 + c2 + a1)
                q1 = 1 - q2
                s2 = [q1, q2]
                s1 = []
                for i in range(M):
                    if (i != cor1[0][1]) & (i != cor2[0][1]):
                        s1.append(0)
                    if (i == cor1[0][1]):
                        s1.append(p1)
                    if (i == cor2[0][1]):
                        s1.append(p2)
                return n2_2m(mat, v, s1, s2)




