from utils.api import get_input
import contextlib

input_str = get_input(9)

def get_next_value(arr, get_prev=False):
    diff_arr = [arr]
    while any([v != 0 for v in diff_arr[-1]]):
        diff_arr.append([n - p for p, n in zip(diff_arr[-1][:-1], diff_arr[-1][1:])])

    if not get_prev:
        for i in range(len(diff_arr) - 1, 0, -1):
            diff_arr[i - 1].append(diff_arr[i][-1] + diff_arr[i-1][-1])
    else:
        for i in range(len(diff_arr) -1, 0, -1):
            diff_arr[i - 1] = [diff_arr[i-1][0] - diff_arr[i][0]] + diff_arr[i-1]

    return diff_arr[0][-1] if not get_prev else diff_arr[0][0]

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    string_arr = input_str.split("\n")[:-1]
    res = 0
    for line in string_arr:
        val = get_next_value([int(i) for i in line.split(" ")])
        print(res)
        res += val
    print(res)

    res = 0
    for line in string_arr:
        val = get_next_value([int(i) for i in line.split(" ")], True)
        print(res)
        res += val
    print(res)



with open("outputs/day_09.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
