from collections import Counter
from utils.api import get_input
import contextlib

input_str = get_input(2)

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    str_arr = input_str.split("\n")
    str_arr = str_arr[:-1]
    max_box = {
            "red": 12,
            "green": 13,
            "blue": 14
            }
    max_box = Counter(max_box)
    
    res = 0
    for idx, game in enumerate(str_arr):
        game_id = idx + 1
        game_res = game.split(":")[-1].strip()
        game_rounds = [i.strip() for i in game_res.split(";")]
        possible = True
        for round in game_rounds:
        
            round_counter = Counter()
    
            round_arr = [i.strip() for i in round.split(",")]
            
    
            for word in round_arr:
                arr = word.split(" ")
                round_counter[arr[1]] += int(arr[0])

            if not (round_counter <= max_box):
                possible = False
                break

        if possible:
            res += game_id
    print("part one")
    print(res)
        
    res = 0
    for idx, game in enumerate(str_arr):
        game_id = idx + 1
        game_res = game.split(":")[-1].strip()
        game_rounds = [i.strip() for i in game_res.split(";")]
        possible = True
        max_vals = {"red": 0, "green": 0, "blue": 0}
        for round in game_rounds:
        
            round_counter = Counter()
    
            round_arr = [i.strip() for i in round.split(",")]
            
            for word in round_arr:
                arr = word.split(" ")
                max_vals[arr[1]] = max(max_vals[arr[1]], int(arr[0]))

        power = 1
        for v in max_vals.values():
            power *= v
        res += power
    print("part two")
    print(res)


with open("outputs/day_02.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
