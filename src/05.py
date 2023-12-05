from collections import deque
from itertools import pairwise
import pandas as pd
from tqdm import tqdm
from utils.api import get_input
import contextlib

input_str = get_input(5)

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    string_arr = input_str.split("\n")
    print(string_arr[-1])
    string_arr = string_arr[:-1]
    seeds = string_arr[0]
    maps = []
    for idx, line in enumerate(string_arr[2:], start=2):
        if "map" in line:
            maps.append([])
            continue
        if line:
            maps[-1].append(line)

    seeds = seeds.split(":")[1].strip()

    location = set()
    for seed in seeds.split(" "):
        # start converting
        seed = int(seed)
        current = seed
        for map in maps:
            map_start = 0
            new = 0
            for l in map:
                new_start, start, r = l.split(" ")
                start, new_start, r = int(start), int(new_start), int(r)
                if start <= current < start + r:
                    map_start = start
                    new = new_start
                    break

            current = (current - map_start) + new

        location.add(current)
    print(location)
    print(min(location))


    location = set()
    seeds = seeds.split(" ")
    new_seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    combined_ranges = set()

    def overlaps(a, b, c, d):
        return not (a > d or b < c)

    intervals = deque([(int(seed), int(seed) + int(m) - 1) for seed, m in new_seeds])

    if intervals:
        # start converting
        for map in maps:
            # check if any of the conversion falls within the intervals
            mapped_ranges = deque()
            while intervals:
                s, e = intervals.popleft()
                added = False
                for l in map:
                    dst, src, sz = l.split(" ")
                    dst, src, sz, = int(dst), int(src), int(sz)
                    start, end = src, src + sz - 1
                    delta = dst - src

                    if not overlaps(s, e, start, end):
                        continue

                    if start <= s <= end and start <= e <= end:
                        mapped_ranges.append((s + delta, e + delta))
                        break

                    if start <= e <= end:
                        mapped_ranges.append((start + delta, e + delta))
                        intervals.append((s, start - 1))
                        break

                    if start <= s <= end:
                        mapped_ranges.append((s + delta, end + delta))
                        intervals.append((end + 1, e))
                        break

                    if s < start and e > end:
                        mapped_ranges.append((start + delta, end + delta))
                        intervals.extend(((end + 1, e), (s, start - 1)))
                        break

                else:
                    mapped_ranges.append((s, e))
                # If so, we need to create new candidates
            intervals = mapped_ranges


    print(min(intervals, key=lambda x: x[0])[0]) 

    # now convert it back
    current = min(intervals, key=lambda x: x[0])[0] 
    for map in maps[::-1]:
        map_start = 0
        new = 0
        for l in map:
            start, new_start, r = l.split(" ")
            start, new_start, r = int(start), int(new_start), int(r)
            if start <= current < start + r:
                map_start = start
                new = new_start
                break

        current = (current - map_start) + new
    print(current)



with open("outputs/day_05.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
