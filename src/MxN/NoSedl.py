import numpy as np

class Matrix_2x2:

    def __init__(self, array):
        self.array = array
        self.a = 0
        self.b = 0
        self.Sa = []
        self.Sb = []
        self.v = 0

    def sed_point(self):
        if (len(np.unique(self.array) != 4) and min(np.max(self.array, axis=0))==max(np.min(self.array, axis=1))):
            while True:
                self.array = np.random.randint(0, 50, (2, 2))
                if len(np.unique(self.array) != 4) == 4 and min(np.max(self.array, axis=0))!=max(np.min(self.array, axis=1)):
                    break
        #self.print()
        self.a = min(np.max(self.array, axis=0))
        # print(f"A = {self.a}")
        self.b = max(np.min(self.array, axis=1))
        # print(f"B = {self.b}")
        self.mixed_strategy()


    def mixed_strategy(self):
        V_c = (self.array[0][0] * self.array[1][1]) - (self.array[0][1] * self.array[1][0])
        znam = self.array[0][0] + self.array[1][1] - self.array[0][1] - self.array[1][0]
        if znam == 0:
            self.sed_point(a)
        p1 = (self.array[1][1] - self.array[1][0]) / znam
        p2 = 1 - p1
        q1 = (self.array[1][1] - self.array[0][1]) / znam
        q2 = 1 - q1
        V = V_c / znam
        self.Sa.append(round(p1, 3))
        self.Sa.append(round(p2, 3))
        self.Sb.append(round(q1, 3))
        self.Sb.append(round(q2, 3))
        self.v = round(V, 3)

        # print(f"Округленное Sa= {self.Sa}")
        # print(f"Округленное Sb= {self.Sb}")
        # print(f"V=({self.v})")


    def print(self):
        print(self.array)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #2x2
    for i in range(1000):
        a = np.random.randint(0, 50, (2, 2))
        play = Matrix_2x2(a)
        play.sed_point()
