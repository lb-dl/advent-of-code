'''
Calculate the horizontal position and depth you would have after following the planned course
https://adventofcode.com/2021/day/2
'''


d = {}

with open('task2.txt', 'r') as file:
    for line in file.readlines():
        (key, val) = line.split()
        d[key] = d.get(key, 0) + int(val)
    print(d)
    for k, v in d.items():
        if k == 'down':
            down = d[k]
        elif k == 'up':
            up = d[k]
        else:
            forward = d[k]
    print((down - up)*forward)
