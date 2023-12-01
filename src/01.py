from utils.api import get_input
import contextlib

input_str = get_input(1)

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    res = 0
    str_list = input_str.split("\n")
    str_list = str_list[:-1]
    for string in str_list:
        num_str = ""
        for c in string:
            if c.isnumeric():
                num_str += c
        
        res += int(num_str[0] + num_str[-1])
    print("part one")
    print(res)

    print("part two")
    numbers = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
            }
    res = 0
    for string in str_list:
        num_str = []
        for i, c in enumerate(string):
            if c.isnumeric():
                num_str.append(int(c))
                continue
            # check if next set of values are equal
            for k, v in numbers.items():
                l = len(k)
                if i + l <= len(string):
                    if k == string[i:i + l]:
                        num_str.append(v)

        res += int(str(num_str[0]) + str(num_str[-1]))
    print(res)




with open("outputs/day_01.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
