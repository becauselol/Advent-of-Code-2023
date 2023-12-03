import re
from utils.api import get_input
import contextlib

input_str = get_input(3)

def solve(input_str):
    string_arr = input_str.split("\n")
    string_arr = string_arr[:-1]
    # WRITE YOUR SOLUTION HERE
    res = 0
    for idx, line in enumerate(string_arr):
        for match in re.finditer(r"\d+" ,line):
            start, end = match.span()
            end = end - 1
            # check surrounding to see if there is
            if idx == 0:
                directions = [1]
            elif idx == len(string_arr) - 1:
                directions = [-1]
            else:
                directions = [1, -1]
            if start > 0 and line[start - 1] != ".":
                res += int(match.group())
                continue
            if end < len(line) - 1 and line[end + 1] != ".":
                res += int(match.group())
                continue
            found = False
            for d in directions:
                for j in range(max(0, start - 1), min(end + 2, len(line))):
                    if not(string_arr[d + idx][j].isnumeric()) and string_arr[d + idx][j] != ".":
                        found = True

                    if found:
                        break
                if found:
                    break

            if found:
                res += int(match.group())

    print("part one")
    print(res)
    
    res = 0
    for idx, line in enumerate(string_arr):
        for match in re.finditer(r"\*", line):
            # check that above and below don't have
            i, _ = match.span()

            number_of_digits = 0
            dig_dir = []
            for xx, yy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= idx + xx < len(string_arr) and 0 <= i + yy < len(line):
                    if string_arr[idx + xx][i + yy].isnumeric():
                        number_of_digits += 1
                        dig_dir.append((xx, yy))

            if number_of_digits > 2:
                continue
            # then check diagonal directions
            # bottom directions
            if (1, 0) not in dig_dir:
                for xx, yy in [(1, 1), (1, -1)]:
                    if 0 <= idx + xx < len(string_arr) and 0 <= i + yy < len(line):
                        if string_arr[idx + xx][i + yy].isnumeric():
                            number_of_digits += 1
                            dig_dir.append((xx, yy))

            if (-1, 0) not in dig_dir:
                for xx, yy in [(-1, 1), (-1, -1)]:
                    if 0 <= idx + xx < len(string_arr) and 0 <= i + yy < len(line):
                        if string_arr[idx + xx][i + yy].isnumeric():
                            number_of_digits += 1
                            dig_dir.append((xx, yy))

            if number_of_digits != 2:
                continue

            nums = [None, None]
            print(dig_dir)
            for k, (xx, yy) in enumerate(dig_dir):
                start = string_arr[idx + xx][i + yy]
                num = start
                t = 1
                while i + yy + t < len(line) and string_arr[idx + xx][i + yy + t].isnumeric():
                    print(string_arr[idx + xx][i + yy + t])
                    num += string_arr[idx + xx][i + yy + t]
                    t += 1

                t = -1
                while i + yy + t < len(line) and string_arr[idx + xx][i + yy + t].isnumeric():
                    print(string_arr[idx + xx][i + yy + t])
                    num = string_arr[idx + xx][i + yy + t] + num
                    t -= 1
                nums[k] = num

            print(nums)
            res += (int(nums[1]) * int(nums[0]))




    print("part two")
    print(res)


with open("outputs/day_03.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
