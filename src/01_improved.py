import re
from utils.api import get_input
import contextlib

input_str = get_input(1)

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    res = 0
    str_list = input_str.split("\n")
    str_list = str_list[:-1]
    for string in str_list:
        first = re.search("[0-9]+", string)
        last = re.search("[0-9]+", string[::-1])
        
        res += int(first.group()[0] + last.group()[0])
    
    print("part one")
    print(res)

    numbers = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
            ]

    reversed_numbers = [s[::-1] for s in numbers]
    res = 0
    forward_expr = f"(\\d|{'|'.join(numbers)})"
    backward_expr = f"(\\d|{'|'.join(reversed_numbers)})"
    for string in str_list:
        first = re.search(forward_expr, string)
        last = re.search(backward_expr, string[::-1])

        if first.group()[0].isnumeric():
            f = int(first.group()[0])
        else:
            f = numbers.index(first.group()) + 1

        if last.group()[0].isnumeric():
            l = int(last.group()[0])
        else:
            l = reversed_numbers.index(last.group()) + 1

        res += (f * 10 + l)
    
    print("part two")
    print(res)






with open("outputs/day_01_improved.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
