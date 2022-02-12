'''
Use the binary numbers in your diagnostic report
to calculate the gamma rate and epsilon rate, then multiply them together
Use the binary numbers in your diagnostic report
to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together
https://adventofcode.com/2021/day/3
'''



from copy import deepcopy


def read_file(path):
    # read a file to add all numbers into a list
    with open(path, 'r') as file:
        list_ = list(file.readlines())
    return list_


def count_power_consump(n, l):
    l1 = []
    # create a dictionary, a number of keys is equal to a number of 'bits'
    # e.g. 111110110000 has 12 'bits'
    d = {}
    d = d.fromkeys([i for i in range(1, n+1)], '')
    # create n numbers, where 1st number has the first bit of each number of a list and so on...
    for i in range(len(l)):
        for j in range(n):
            d[j+1] += l[i][j]

    # count the most common 'bit' in each number
    for k, v in d.items():
        if sum([i == '1' for i in v]) > len(l)//2:
            l1.append('1')
        else:
            l1.append('0')

    # create a str from dictionary values
    gamma_rate = ''.join([el for el in l1])
    # creat an 'inverse' str from 'gamma_rate', e.g. '1101' -> '0010'
    epsilon_rate = ''.join([str(1 - int(el)) for el in gamma_rate])
    res = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return res


def calculate_oxygen_rate(l):
    ones = []
    zeros = []
    i = 0
    while len(l) > 1:
        for n in l:
            if n[i] == '1':
                ones.append(n)
            else:
                zeros.append(n)
        if len(ones) >= len(zeros):
            l = deepcopy(ones)
        else:
            l = deepcopy(zeros)
        i += 1
        ones.clear()
        zeros.clear()
    return int(l[0], 2)


def calculate_co2_rate(l):
    ones = []
    zeros = []
    i = 0
    while len(l) > 1:
        for n in l:
            if n[i] == '1':
                ones.append(n)
            else:
                zeros.append(n)
        if len(zeros) <= len(ones):
            l = deepcopy(zeros)
        else:
            l = deepcopy(ones)
        i += 1
        ones.clear()
        zeros.clear()
    return int(l[0], 2)


list_ = read_file('task3.txt')

print(count_power_consump(12, list_))

life_support_rating = calculate_oxygen_rate(list_) * calculate_co2_rate(list_)

print(life_support_rating)

# l = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
