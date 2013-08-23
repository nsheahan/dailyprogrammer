import random
import sys


def gen_ops(num):
    random.seed()
    ops = ['+', '-', '*']
    ret_ops = []
    for i in range(num):
        ret_ops.append(ops[random.randrange(0, num)])

    return ret_ops


def gen_nums(lbound, ubound, num):
    random.seed()
    ret_nums = []
    interval = list(range(lbound, ubound))
    for i in range(num):
        ret_nums.append(interval[random.randrange(lbound, ubound)])

    return ret_nums

while 1:
    len_expression = 4
    ops = gen_ops(len_expression - 1)
    nums = gen_nums(0, 15, len_expression)

    index = 1
    for op in ops:
        nums.insert(index, op)
        index += 2

    expression = ''.join(str(e) for e in nums)
    answer = eval(expression)

    print(expression)
    guess = input("")

    if guess == 'q' or guess == 'Q':
        break
    elif guess == str(answer):
        print("Correct")
    else:
        print("Incorrect")



