# This is a sample Python script.
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

class Matrix_2x2:

    def __init__(self, array):
        self.array = array

    def sed_point(self):
        position = []
        Sa = [0, 0]
        Sb = [0, 0]
        if (len(np.unique(self.array) != 4)):
            while True:
                self.array = np.random.randint(0, 20, (2, 2))
                if len(np.unique(self.array) != 4) == 4:
                    break
        self.print()
        max_in_columns = np.max(self.array, axis=0)
        a = min(max_in_columns)
        print(f"A = {a}")
        # Нахождение минимума в каждой строке
        min_in_rows = np.min(self.array, axis=1)
        b = max(min_in_rows)
        print(f"B = {b}")
        if (a == b):
            for i in range(len(self.array)):
                for j in range(len(self.array)):
                    if self.array[i][j] == a:
                        position.append(i)
                        position.append(j)
            pos = np.where(self.array == a)
            r = pos[0][0]  # Индексы строк
            c = pos[1][0] # Индексы столбцов
            Sa[r] = 1
            Sb[c] = 1
            print("Седловая точка: A{}B{}".format(position[0]+1, position[1]+1))
            print(f"Sa= ({Sa[0]}, {Sa[1]})  Sb=({Sb[0]}, {Sb[1]})")
        else:
            self.mixed_strategy()

    def mixed_strategy(self):
        V_c = (self.array[0][0] * self.array[1][1]) - (self.array[0][1] * self.array[1][0])
        znam = self.array[0][0] + self.array[1][1] - self.array[0][1] - self.array[1][0]
        p1 = (self.array[1][1] - self.array[1][0]) / znam
        p2 = 1 - p1
        q1 = (self.array[1][1] - self.array[0][1]) / znam
        q2 = 1 - q1
        V = V_c / znam
        print(f"Sa=({p1},{p2})  Sb=({q1},{q2})")
        p11 = p1  # Если делать округление до 3 знаков после запятой
        p22 = p2
        q11 = q1
        q22 = q2
        print(f"Округленное Sa=({round(p11, 3)},{round(p22, 3)})")
        print(f"Округленное Sb=({round(q11, 3)},{round(q22, 3)})")
        print(f"V=({round(V, 3)})")
    def print(self):
        print(self.array)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #2x2
    a = np.random.randint(0, 20, (2, 2))
    play = Matrix_2x2(a)
    play.sed_point()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
