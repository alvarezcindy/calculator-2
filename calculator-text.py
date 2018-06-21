"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
from functools import reduce

math_file = open("inputs.txt")

def calculate(math_file):
    ans_list = []
    for line in math_file:
        line = line.rstrip()
        token = line.split(" ")

        operator = token[0]
        numbers = "".join(token[1:])

        if numbers.isdigit():
            float_list = [float(i) for i in token[1:]]
        else:
            continue

        if operator == "pow":
            answer = reduce(power, float_list)
        elif operator == '+':
            answer = reduce(add, float_list)
        elif operator == '-':
            answer = reduce(subtract, float_list)
        elif operator == '*':
            answer = reduce(multiply, float_list)
        elif operator == '/':
            answer = reduce(divide, float_list)
        elif operator == 'square':
            answer = reduce(square, float_list)
        elif operator == 'cube':
            answer = reduce(cube, float_list)
        elif operator == 'mod':
            answer = reduce(mod, float_list)
        else:
            continue

        ans_str = round(answer, 2)
        ans_list.append(ans_str)
    return ans_list


def calc_outputs(ans_list):
    with open("outputs.txt", 'w') as f:
        for item in ans_list:
            f.write("{}\n".format(str(item)))


calc_list = calculate(math_file)
calc_outputs(calc_list)
