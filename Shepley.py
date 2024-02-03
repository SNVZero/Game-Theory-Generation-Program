import random
from itertools import permutations
from math import factorial


class Shepley_vector:
    def __init__(self, function, n):
        self.function = function
        self.n = n
        self.vector_find = []
        self.core = " "

    def player_profit(self, coalition, player):
        with_player = function.get(coalition)  # Получение значения ключа
        without_player = function.get(coalition.replace(str(player), ''), 0)  # Удаление строки игрока, иначе 0. Было 123, стало 23
        return with_player - without_player

    def summ_fact(self, n, coalition):
        fact_ns = factorial(n - len(coalition))  # (n-|s|)!
        fact_s = factorial(len(coalition) - 1)  # (|s|-1)!
        fact_n = factorial(n)  # n!
        return (fact_ns * fact_s) / fact_n

    def find_vecotr(self):
        vector = []
        flag = False
        for i in range(self.n):
            value = 0
            player = i + 1

            for key in function.keys():
                if str(player) in key:
                    value += self.summ_fact(self.n, key) * self.player_profit(key, player)
            vector.append(value)
        if (vector[0]+vector[1]+vector[2] <= function.get('123')+0.5 and vector[0]+vector[1]+vector[2] >= function.get('123')-0.5):
            if (vector[0]>= function.get('1') and vector[0] <= function.get('123')-function.get('23')):
                if (vector[1]>= function.get('2') and vector[1] <= function.get('123')-function.get('13')):
                    if (vector[2] >= function.get('3') and vector[2] <= function.get('123') - function.get('12')):
                        flag = True
        self.vector_find = vector
        self.print(vector, flag)

    def print(self, vector, flag):
        print("Вектор Шепли: " + str(vector))
        if flag == True:
            self.core = "Вектор принадлежит ядру"
            print(self.core )
        else:
            self.core = "Вектор не принадлежит ядру"
            print(self.core )

if __name__ == '__main__':
    #2x2
    '''
    function = {
       '1': 230,
        '2': 150,
        '3': 170,
        '12': 420,
        '13': 470,
        '23': 350,
        '123': 600
    }'''
    function = {}
    for i in range(1, 4):
        function[str(i)] = random.randint(100, 400)
    function['12'] = function['1'] + function['2'] + random.randint(20, 200)
    function['13'] = function['1'] + function['3'] + random.randint(20, 200)
    function['23'] = function['2'] + function['3'] + random.randint(20, 200)
    function['123'] = function['1'] + function['2'] + function['3'] + random.randint(20, 200)
    print(f"Входные данные: {function}")
    vec = Shepley_vector(function, 3)
    vec.find_vecotr()

'''A, B, a, b = [], [], [], []
for i in range(2):
    A.append(random.sample(range(21), 2))
    B.append(random.sample(range(21), 2))
Flag = False
A = np.array(A)
B = np.array(B)
row_max = np.argmax(A, axis=1)
col_max = np.argmax(B, axis=0)
print(row_max)
print(col_max)
if (row_max[0]== col_max[0] or row_max[1]== col_max[1] ):
    Flag = True
print(Flag)
print(f"A = {A}")
print(" ")
print(f"B = {B}")
game2 = nashpy.Game(A,B)
#print(game2)

# Find the Nash Equilibrium with Support Enumeration
equilibria = game2.support_enumeration()
for eq in equilibria:
    print(eq)
    if (eq[0][0] == 1):
        a.append(0)
    elif (eq[0][0] == 0):
        a.append(1)
    if (eq[1][0] == 1):
        b.append(0)
    elif (eq[1][0] == 0):
        b.append(1)
for i in range(len(a)):
    print(f"A{a[i]+1}B{b[i]+1}")'''