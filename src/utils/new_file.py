import os

l = filter(lambda x: "__" not in x and ".py" in x, os.listdir("src"))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

DEFAULT_FILE = f"""from utils.api import get_input
import contextlib

input_str = get_input(1)

def solve(input_str):
    # WRITE YOUR SOLUTION HERE


with open("outputs/day_{n:02d}.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
"""

path = f"src/{n:02d}.py"
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
