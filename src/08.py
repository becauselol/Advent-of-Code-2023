import math, itertools
from collections import defaultdict
from utils.api import get_input
import contextlib

input_str = get_input(8)
print("WHAT")

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    string_arr = input_str.split("\n")
    string_arr = string_arr[:-1]
    steps = string_arr[0]
    string_arr = string_arr[2:]
    
    dd = defaultdict(dict)
    for line in string_arr:
        start, nodes = line.split("=")
        start, nodes = start.strip(), nodes.strip()
        l, r = nodes.split(",")
        l, r = l.strip(), r.strip()
        dd[start]["L"] = l[1:]
        dd[start]["R"] = r[:-1]

    n = len(steps)
#    res = 0
#    node = "AAA"
#    
#    while node != "ZZZ":
#        print(node, dd[node])
#        node = dd[node][steps[res % n]]
#        res += 1
#    print(res)

    def length(node, is_end = lambda node: node.endswith("Z")):
        for index, move in enumerate(itertools.cycle(steps)):
            if is_end(node):
                return index
            node = dd[node][move]

    print(math.lcm(*(length(node) for node in dd if node.endswith("A"))))

#   nodes = [k for k in dd.keys() if k[-1] == "A"]
#   res = 0
#   while any([n[-1] != "Z" for n in nodes]):
#       for i in range(len(nodes)):
#           nodes[i] = dd[nodes[i]][steps[res % n]]
#       res += 1
#   print(res)



with open("outputs/day_08.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
