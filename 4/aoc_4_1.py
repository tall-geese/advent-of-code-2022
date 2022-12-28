
# How many of a single elf's sections are fully contained inside the partner elf's section

    # Psuedo
# If one of the one of the lists is exactly one element, then check
# if that number falls within the range created by the other

# When creating the ends of the list, check that both numbers arent exactly the same
    # If they are then we only need to create a list of that one number, otherwise
    # We can create a list of range(x, y + 1)

# If there is more than a single element, then
    # if elf1's lbound is greater than elf2's lbound (positive number or 0)
    # if that difference plus its len is less than or equal to the other elf's len
    # then its good.

    # If the number is negative..
    # that perform the same check, but mix up the test parameters

err_pairs = 0

def is_contained(inside_list, outside_list) -> bool:
    # diff = inside_list[0] - outside_list[0] # should be positive or zero if we got this far
    return inside_list[0] >= outside_list[0] and inside_list[-1] <= outside_list[-1]


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    

for line in lines:
    elves = [elf1, elf2] = line.split(',')
    for ind, elf in enumerate(elves):
        elf = [low, high] = elf.split('-')
        elf = list(range(int(low), int(high) + 1))
        elves[ind] = elf

    # The one with the larger or equal lbound has a shot at being contained
    # keep that one on the left, if smaller than we switch positions
    
    elf1, elf2 = elves
    # we need something here in case that the lbounds are the same
    # newed to proceed to check that the ubounds are different, switch to have the smaller ubound on the left
    if elf1[0] == elf2[0]:
        if elf1[-1] > elf2[-1]:
            elves = elf2, elf1
    if elf1[0] < elf2[0]:
        elves = elf2, elf1
    
    if (len(elf1) == 1 and elf1[0] in elf2) or (len(elf2) == 1 and elf2[0] in elf1):
        err_pairs += 1
    elif is_contained(*elves):
        err_pairs += 1
    else:
        pass
        # print('not contained')
        # print(elves)


print(err_pairs)