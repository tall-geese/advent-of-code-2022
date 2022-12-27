# 2nd scenario
# X means lose
# Y means draw
# Z means win


# So if its a 'Y' then we need to 
    # return with out play pooints(matching the user's input)
    # and then add 3 to that

# if i need to loseif their exact number is a 'A'
#     then  i need a 'C', otherwise its going to be their input -1

# if i need to win then
#     if they have a 'C' sciccors, then i need a rock, their input - 2
#     otherwise, i need their input + 1

def determine_scrore(line: str) -> int:
    opp, me = line.split(' ')
    
        
    if me == 'Y':  # If we need a tie
        return selection_points(ord(opp)) + 3
    elif me == 'X': # If we need to lose
        return selection_points(get_loss(opp)) + 0
    else: # If we need to win
        return selection_points(get_win(opp)) + 6 

def selection_points(input: int) -> int:
    return input - 64

def get_loss(opp: str) -> int:
    if opp == 'A':
        return ord('A') + 2
    else:
        return ord(opp) - 1

def get_win(opp: str) -> int:
    if opp == 'C':
        return ord('C') - 2
    else:
        return ord(opp) + 1


if __name__ == '__main__':
    with open('input.txt') as input:
        lines = input.read().split('\n')

    print(sum(map(determine_scrore, lines)))