from django.test import TestCase

# Create your tests here.
dic = {
    'name': 'asdf',
    'age': 18,
    'gender': 'male',
    'job': 'student'
}
lst = sorted(dic.items(), key=lambda i: i[0])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in a if i % 2 == 1]

import datetime

a = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "星期" + str(datetime.datetime.now().isoweekday())
import re

s = "info:xiaozhang 33 sehenz"
res1 = re.split(r":| ", s)


# print(res1)

def get_sum(num):
    if num >= 1:
        res2 = num + get_sum(num - 1)
    else:
        res2 = 0
    return res2


def get_stair(num):
    if num == 1:
        res3 = 1
    elif num == 2:
        res3 = 2
    elif num == 3:
        res3 = 4
    else:
        res3 = get_stair(num - 1) + get_stair(num - 2) + get_stair(num - 3)
    return res3


"""
1111
112
121
211
22
"""
lst1 = [1, 23, 4, 6, 7, 22]
lst2 = [1, 22, 5, 8, 9]

lst3 = list(set(lst1).intersection(set(lst2)))
jj = [i for i in lst1 if i in lst2]
lst4 = list(set(lst1).union(set(lst2)))
lst5 = list(set(lst1).difference(set(lst2)))
lst6 = list(set(lst2).difference(set(lst1)))

s = "小米今年18岁，工资8000"
# tes = re.search(r"\d+",s).group()
# tes = re.findall(r"\d+",s)
tes = re.match("小米", s).group()

from functools import wraps


class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class president(metaclass=SingletonMeta):
    pass


def singleton(cls):
    instance = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


@singleton
class President:
    pass


lstt = [1, 4, 6, 2, 1, 7, 22, 12, 45, "123"]

lstt1 = set(lstt)

import copy

la = [[1, 2], 1, 4, 6, 2, 1, 7, 22, 12, 45]
lc = copy.copy(la)
ld = copy.deepcopy(la)
la.append(2)
la[0][0] = 2


def febona(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def feibonacc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return feibonacc(n - 1) + feibonacc(n - 2)


s = range(4)


def sss():
    return [lambda x, i=i: i * x for i in range(4)]


# print([m(100) for m in sss()])

def count_letters(items):
    result = {}
    for item in items:
        # if isinstance(item, (int,float)):
        result[item] = result.get(item, 0) + 1
    return result


import os

g = os.walk('/usr/local/')

for path, dir_list, file_list in g:
    for dir_name in dir_list:
        pass
    #     print(os.path.join(path,dir_name))
    for file_name in file_list:
        pass
        # print(os.path.join(path,file_name))

from functools import lru_cache


@lru_cache()
def change_money(num):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    else:
        return change_money(num - 2) + change_money(num - 3) + change_money(num - 5)


# print(change_money(2))
def get_st(num):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    else:
        return get_st(num - 1) + get_st(num - 2) + get_st(num - 3)


# print(len({x for x in 'hello world' if x not in 'abcdefg'}))

def show_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    row, col = 0, 0
    num, direction = 1, 0
    while num <= n ** 2:
        if matrix[row][col] == 0:
            matrix[row][col] = num
            num += 1
        if direction == 0:
            if col < n - 1 and matrix[row][col + 1] == 0:
                col += 1
            else:
                direction += 1
        if direction == 1:
            if row < n - 1 and matrix[row + 1][col] == 0:
                row += 1
            else:
                direction += 1
        if direction == 2:
            if col > 0 and matrix[row][col - 1] == 0:
                col -= 1
            else:
                direction += 1
        if direction == 3:
            if row > 0 and matrix[row - 1][col] == 0:
                row -= 1
            else:
                direction += 1
        direction %= 4


    for x in matrix:
        for y in x:
            print(y, end='\t')
        print()

show_spiral_matrix(2)
show_spiral_matrix()
show_spiral_matrix(4)