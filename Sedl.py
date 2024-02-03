import numpy as np

class Matrix_2x2:

    def __init__(self, array):
        self.array = array

    def sed_point(self):
        position = []
        Sa = [0, 0]
        Sb = [0, 0]
        if (len(np.unique(self.array) != 4) and min(np.max(self.array, axis=0))!=max(np.min(self.array, axis=1))):
            while True:
                self.array = np.random.randint(0, 50, (2, 2))
                if len(np.unique(self.array) != 4) == 4 and min(np.max(self.array, axis=0))==max(np.min(self.array, axis=1)):
                    break
        self.print()
        a = min(np.max(self.array, axis=0))
        print(f"A = {a}")
        b = max(np.min(self.array, axis=1))
        print(f"B = {b}")
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if self.array[i][j] == a:
                    position.append(i)
                    position.append(j)
        pos = np.where(self.array == a)
        r = pos[0][0]  # Индексы строк
        c = pos[1][0]  # Индексы столбцов
        Sa[r] = 1
        Sb[c] = 1
        print("Седловая точка: A{}B{}".format(position[0] + 1, position[1] + 1))
        print(f"Sa= ({Sa[0]}, {Sa[1]})  Sb=({Sb[0]}, {Sb[1]})")

    def print(self):
        print(self.array)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #2x2
    a = np.random.randint(0, 50, (2, 2))
    play = Matrix_2x2(a)
    play.sed_point()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
