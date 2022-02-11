"""
Bingo. Part 1
Board is a winner if it has at least one complete row or column of marked numbers
Final score is calculated by multiplying 'sum of all unmarked numbers on that board' and last called number
https://adventofcode.com/2021/day/4
"""


from itertools import chain


def read_file(path):
    with open(path, 'r') as file:
        # add lines without trailing '\n' and skip empty lines, e.g. '59 98 84 27 56\n' -> '59 98 84 27 56'
        lines = [l.rstrip() for l in file.readlines() if l.strip()]
        first_line_of_num = [int(s) for s in lines[0].split(',')]
        # turn strings into lists of numbers, e.g. '59 98 84 27 56' -> [59, 98, 84, 27, 56]
        list_of_numbers = [[int(s) for s in str_.split()] for str_ in lines[1:]]
        # creat a list of 'list_of_boards', consisting of 25 first_line_of_num
        list_of_boards = []
        for i in range(0, len(list_of_numbers), 5):
            list_of_boards.append(list(chain.from_iterable(list_of_numbers[i:i + 5])))

    return list_of_boards, first_line_of_num


def is_a_winner(list_):
    start = 0
    for i in range(5):
        if list_[i] + list_[i + 1] + list_[i + 2] + list_[i + 3] + list_[i + 4] == 500:
            return True
        start += 5
    for i in range(5):
        if list_[i] + list_[i + 5] + list_[i + 10] + list_[i + 15] + list_[i + 20] == 500:
            return True
        start += 1
    return False


data = read_file('task4.txt')
boards, numbers = data
print(boards, numbers)

flag = False
while flag == False:
    number = numbers[0]
    numbers = numbers[1:]

    for board in boards:
        for i in range(len(board)):
            if board[i] == number:
                board[i] = 100

    for board in boards:
        if is_a_winner(board):
            sum_of_unmarked = sum([n for n in board if n != 100])
            score = sum_of_unmarked * number
            flag = True
