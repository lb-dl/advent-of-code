"""
Bingo. Part 1
Board is a winner if it has at least one complete row or column of marked numbers
Final score is calculated by multiplying 'sum of all unmarked numbers on that board' and last called number
https://adventofcode.com/2021/day/4
"""


def read_file(path):
    with open(path, 'r') as file:
        # add lines without trailing '\n' and skip empty lines, e.g. '59 98 84 27 56\n' -> '59 98 84 27 56'
        lines = [l.rstrip() for l in file.readlines() if l.strip()]
        return lines


def creat_list_of_rows(list_):
    list_of_rows = [list_[i:i + 5] for i in range(0, len(list_), 5)]
    return list_of_rows


def swap_rows_with_columns(l):
    l1 = [list(x) for x in zip(*l)]
    return l1


def is_a_winner(l, n, m):
    for i in range(m):
        if n in l[i]:
            l[i].remove(n)
        if not l[i]:
            return True


list_of_lines = read_file('task4.txt')
first_line_of_num = [int(s) for s in list_of_lines[0].split(',')]
list_of_numbers = [[int(s) for s in str_.split()] for str_ in list_of_lines[1:]]

rows = creat_list_of_rows(list_of_numbers)
columns = []
for i in range(len(rows)):
    columns.append(swap_rows_with_columns(rows[i]))


found_a_winner = False
for n in first_line_of_num:
    for i in range(len(rows)):
        if is_a_winner(rows[i], n, 5):
            score = sum([sum(n) for n in rows[i]])
            total_score = score * n
            print(f'total_score: {total_score}')
            found_a_winner = True
        elif is_a_winner(columns[i], n, 5):
            score = sum([sum(n) for n in columns[i]])
            total_score = score * n
            print(f'total_score: {total_score}')
            found_a_winner = True
    if found_a_winner:
        break
