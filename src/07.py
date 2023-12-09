from utils.api import get_input
import contextlib
from collections import Counter

input_str = get_input(7)

card_map = {
        "A": 14,
        "T": 10,
        "K": 13,
        "Q": 12,
        "J": 11
        }
for i in range(2, 10):
    card_map[str(i)] = i

class Card:
    def __init__(self, value, new_rule=False):
        self.value = value
        self.mapped_value = card_map[value]
        if self.value == "J" and new_rule:
            self.mapped_value = 1

    def __lt__(self, other):
        return self.mapped_value < other.mapped_value

hand_value = {
        "Five": 7,
        "Four": 6,
        "Full": 5,
        "Three": 4,
        "TwoP": 3,
        "OneP": 2,
        "High": 1
        }

def get_hand_type(cards, new_rule = False):
    c = Counter(cards)
    if new_rule:
        if "J" in c:
            
            # find the max key
            j_count = c["J"]
            if j_count != 5:
                del c["J"]
                max_key = max(c, key=c.get)
                c[max_key] += j_count
    
    c_count = Counter(c.values())
    if 5 in c_count:
        return "Five"
    if 4 in c_count:
        return "Four"
    if 3 in c_count and 2 in c_count:
        return "Full"
    if 3 in c_count:
        return "Three"
    if 2 in c_count and c_count[2] == 2:
        return "TwoP"
    if 2 in c_count and c_count[2] == 1:
        return "OneP"
    
    return "High"

class Hand:
    def __init__(self, string, new_rule = False):
        self.cards = [Card(c, new_rule) for c in string]
        self.hand_type = get_hand_type(string, new_rule)
        self.hand_type_value = hand_value[self.hand_type]

    def __lt__(self, other):
        
        return (self.hand_type_value, tuple([c.mapped_value for c in self.cards])) < (other.hand_type_value, tuple([c.mapped_value for c in other.cards]))

def solve(input_str):
    # WRITE YOUR SOLUTION HERE
    string_arr = input_str.split("\n")
    string_arr = string_arr[:-1]
    
    hands = []
    bids = []
    for line in string_arr:
        hand, bid = line.split(" ")
        hand, bid = hand.strip(), bid.strip()
        hands.append(Hand(hand))
        bids.append(int(bid))

    overall = list(zip(hands, bids))
    sorted_overall = sorted(overall, key=lambda x: x[0])
    res = 0
    for i, (h, b) in enumerate(sorted_overall):
        res += (b * (i + 1))
    print("part one")
    print(res)

    hands = []
    bids = []
    for line in string_arr:
        hand, bid = line.split(" ")
        hand, bid = hand.strip(), bid.strip()
        hands.append(Hand(hand, True))
        bids.append(int(bid))
 
    overall = list(zip(hands, bids))
    sorted_overall = sorted(overall, key=lambda x: x[0])
    res = 0
    for i, (h, b) in enumerate(sorted_overall):
        res += (b * (i + 1))
    print("part two")
    print(res)


with open("outputs/day_07.txt", "w+") as f:
    with contextlib.redirect_stdout(f):
        solve(input_str)
