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
    for i, line in enumerate(string_arr):
        for j, c in enumerate(line):
            if c != "*":
                continue

            candidates = []
            for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                if 0 <= i + ii < len(string_arr) and 0 <= j + jj < len(line):
                    if string_arr[i + ii][j + jj].isnumeric():
                        t = 1
                        start = string_arr[i + ii][j + jj]
                        while j + jj + t < len(line) and string_arr[i + ii][j + jj + t].isnumeric():
                            start = start + string_arr[i + ii][j + jj + t]
                            t += 1
                        r = j + jj + t - 1

                        t = -1
                        while j + jj + t >= 0 and string_arr[i + ii][j + jj + t].isnumeric():
                            start = string_arr[i + ii][j + jj + t] + start
                            t -= 1
                        l = j + jj + t + 1
                        candidates.append((start, l, r, i + ii))
            candidates = list(set(candidates))
            if len(candidates) == 2:
                res += int(candidates[0][0]) * int(candidates[1][0])


     



    print("part two")
    print(res)


with open("outputs/day_03.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
