from utils.api import get_input
import contextlib

input_str = get_input(4)

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    string_arr = input_str.split("\n")
    string_arr = string_arr[:-1]

    res = 0
    for idx, line in enumerate(string_arr):
        numbers = line.split(":")
        numbers = numbers[1]
        win, card = numbers.split("|")
        win, card = win.strip(), card.strip()
        win = set(win.split(" "))
        win.discard("")
        card = set(card.split(" "))
        card.discard("")

        inter = card.intersection(win)
        if len(inter) > 0:
            res += 2**(len(inter) - 1)
    print("part one")
    print(res)
    
    multiply = [1] * len(string_arr)
    for idx, line in enumerate(string_arr):
        numbers = line.split(":")
        numbers = numbers[1]
        win, card = numbers.split("|")
        win, card = win.strip(), card.strip()
        win = set(win.split(" "))
        win.discard("")
        card = set(card.split(" "))
        card.discard("")

        num_win = len(card.intersection(win))
        for j in range(idx + 1, min(idx + 1 + num_win, len(string_arr))):
            multiply[j] += multiply[idx]

    print("part two")
    print(sum(multiply))

with open("outputs/day_04.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
