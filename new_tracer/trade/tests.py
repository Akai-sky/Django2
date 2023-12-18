from django.test import TestCase


# Create your tests here.
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


import datetime

from functools import wraps
import time


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}执行时间：{time.time() - start}秒')
        return result

    return wrapper


@record_time
def which_day(year, month, date):
    end = datetime.date(year, month, date)
    start = datetime.date(year, 1, 1)
    return (end - start).days + 1


lsss = ['a1', 'a10', 'a2', 'b1', 'b2']

import re


def sort_lsss(ls):
    pattern = re.compile(r'([a-zA-Z]+)([0-9]+)')
    return sorted(ls, key=lambda x: (pattern.match(x).groups()[0], int(pattern.match(x).groups()[1])))


def list_deep(lst):
    if isinstance(lst,list):
        max_depth = 1
        for item in lst:
            max_depth = max(list_deep(item) + 1, max_depth)
        return max_depth
    return 0


from functools import wraps
from random import random
from time import sleep

def retry(*,retry_times=3,max_wait_secs=5, errors=(Exception,)):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retry_times):
                try:
                    return func(*args, **kwargs)
                except errors:
                    sleep(random() * max_wait_secs)
            return None

        return wrapper
    return decorate

class Retry(object):
    def __init__(self, *,retry_times=3,max_wait_secs=5, errors=(Exception,)):
        self.retry_time = retry_times
        self.max_wait_secs = max_wait_secs
        self.errors = errors

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.retry_time):
                try:
                    return func(*args, **kwargs)
                except self.errors:
                    sleep(random() * self.max_wait_secs)
            return None
        return wrapper


def reverse_string(content):
    return content[::-1]

def reverse_string1(content):
    return ''.join(reversed(content))

def reverse_str(content):
    if len(content) <= 1:
        return content
    return reverse_string(content[1:]) + content[0]

def find_dup(items):
    dup = [0] * 9000
    for item in items:
        dup[item - 1000] += 1
    for idx, val in enumerate(dup):
        if val > 1:
            print(idx+1000)
price = {'apple':222,'pair':12,'pork':23}
# print(sorted(price, key=lambda x: price[x], reverse=True))

def more_than_half(items):
    temps, times = None, 0
    for item in items:
        if times == 0:
            temps = item
            times += 1
        else:
            if temps == item:
                times += 1
            else:
                times -= 1
    return temps

from copy import deepcopy, copy


tes = True

asd = not tes
print(asd)