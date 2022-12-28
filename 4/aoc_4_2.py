
# This time we need to check if the lists overlap at all with each other

def pairs_overlap(lower_side, upper_side) -> bool:
    return not (lower_side[-1] < upper_side[0]) 


overlapping_pairs = 0

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    

for line in lines:
    elves = [elf1, elf2] = line.split(',')
    for ind, elf in enumerate(elves):
        elf = [low, high] = elf.split('-')
        elf = list(range(int(low), int(high) + 1))
        elves[ind] = elf

    elf1, elf2 = elves

# if we have any matching lbounds, then they automatically overlap
# otherwise we should get the pair with the lower lbound on the left
    if elf1[0] == elf2[0]:
        overlapping_pairs += 1
        continue
    elif elf1[0] > elf2[0]:
        elves = elf2, elf1

    if pairs_overlap(*elves):
        overlapping_pairs += 1

print(overlapping_pairs)