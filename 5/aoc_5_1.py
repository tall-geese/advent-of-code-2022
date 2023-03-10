
# Start by extracting alkl of the information from the first 9 columns
# and arranging them into a list of lists


import re
from collections import deque

def get_crate_item(item: str)-> str:
    item = item.strip()
    return None if not item else item[1]



pattern = '^' + r'(\[\D\]|\s{3})\s' * 9
pattern = pattern[:-2]
firstLine = True
crates = []

for line in open('input2.txt', 'r'):
    for ind, crate in enumerate(re.search(pattern, line).groups()):
        loot = get_crate_item(crate)
        if firstLine:
            if not loot:
                crates.append(deque([]))
            else:
                crates.append(deque([loot]))
        else:
            if loot: crates[ind].append(loot)
    
    firstLine = False


with open('input.txt', 'r') as file:
    moves = file.read().split('\n')

pattern = '^move (\d+) from (\d) to (\d)'
for ind, move in enumerate(moves):
    boxes, from_pile, to_pile =  re.search(pattern, move).groups()
    from_pile = int(from_pile); to_pile = int(to_pile); boxes = int(boxes)
    from_pile -= 1; to_pile -= 1  # b/c the lists are 0 indexed

    for i in range(boxes):
        try:
            # print(f'\t {i} \t {from_pile} -> {to_pile}')
            loot = crates[from_pile].popleft()
            crates[to_pile].appendleft(loot)
            # crates[to_pile].appendleft(crates[from_pile].popleft())
        except Exception as e:
            print(e)
            quit()

# Print the first letter of each col
for i in crates:
    print(i[0])