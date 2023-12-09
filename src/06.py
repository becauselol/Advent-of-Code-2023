from io import StringIO
from utils.api import get_input
import contextlib

input_str = get_input(6)

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    # r"(\d+):\s+(.*)\s+\|\s+(.*)"
    string_arr = input_str.split("\n")
    string_arr = string_arr[:-1]
    time_arr = [int(i) for i in string_arr[0].split(":")[1].split(" ") if i != ""]
    dist_arr = [int(i) for i in string_arr[1].split(":")[1].split(" ") if i != ""]
    ways_to_beat = []
    for t, d in zip(time_arr, dist_arr):
        ways = 0
        for hold in range(t + 1):
            left = t - hold
            ways += int(left * hold > d)


        ways_to_beat.append(ways)

    res = 1
    for w in ways_to_beat:
        res *= w
    print(res)

    time = int("".join([str(i) for i in time_arr]))
    dist = int("".join([str(i) for i in dist_arr]))

    ways = []
    
    # from start
    for hold in range(time + 1):
        left = time - hold
        if left * hold > dist:
            ways.append(hold)
            break
    for hold in range(time + 2, -1, -1):
        left = time - hold
        if left * hold > dist:
            ways.append(hold)
            break
    print(ways[1] - ways[0] + 1)


with open("outputs/day_06.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
