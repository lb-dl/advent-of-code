'''
Count the number of times a depth measurement increases
from the previous measurement.
(There is no measurement before the first measurement.)
https://adventofcode.com/2021/day/1
'''


def make_list(f):
    depth = []
    with open(f, 'r') as file:
        for line in file.readlines():
            depth.append(int(line))
    return depth


def count_rises(list_):
    counter = sum([1 for i in range(len(list_) - 1) if (list_[i+1] - list_[i]) > 0])
    return counter


print(count_rises(make_list('task1.txt')))
