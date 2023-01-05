
"""
    This time there is the Head and 9 Knots trailing behind
    Needs to keep track of each unique place the 9th knot has visited

    Guessed 650 - too low
    2545 - doneski

"""


def move_left(head) -> tuple[int, int]:
    return (head[0] - 1, head[1])

def move_right(head) -> tuple[int, int]:
    return (head[0] + 1, head[1])

def move_up(head) -> tuple[int, int]:
    return (head[0], head[1] + 1)
def move_down(head) -> tuple[int, int]:
    return (head[0], head[1] - 1)

def update_tail_position(tail, head) -> tuple[int, int]:
    # if the head is at least abs(two) away in any given direction
    # we need to update(add) in that direction 1 (-/+)
        # sign is determined by dividing the distance by itself

    # THEN if its still at aleast 1 away in the other coordinate, we need to
    # udpate that one as well

    for i in [0, 1]:
        dist = head[i] - tail[i]
        if abs(dist) == 2:
            far_assignment = tail[i] + (dist / abs(dist)) # gives neg or positive direction as needed, increment by 1
            other_coord = 0 if i == 1 else 1
            close_assignment = tail[other_coord]

            dist = head[other_coord] - tail[other_coord]
            if abs(dist) >= 1:
                close_assignment += (dist / abs(dist))  # same thing as above

            # Kinda became a mess towards the end
            return (far_assignment, close_assignment) if i == 0 else (close_assignment, far_assignment)

    return tail
            

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')

    # head = (0, 0)
    tails = [(0,0) for i in range(10)]
    history = set([])
    history.add((0,0))

    # print(re.search(pattern, lines[0]).group(1))
    for line in lines:
        direction, spaces = line.split(' ')

        # switch on the direction, assinging a function to a value
        # iterate over the range of the spaces moving in the assigned function each time

        # After every movement, update the position of the tail and if we need to move or not
        # After every movement of the tail, add its current position to the set

        move_func = None
        match direction:
            case 'L':
                move_func = move_left
            case 'R':
                move_func = move_right
            case 'U':
                move_func = move_up
            case 'D':
                move_func = move_down

        for i in range(0, int(spaces)):  # moving in the direction a given number of times
            tails[0] = move_func(tails[0])
            # head = move_func(head)  # move the head
            # print(list(pairwise([head, *tails])))
            for ind, tail in enumerate(tails):
                if ind + 1 == len(tails): 
                    break
                tail = update_tail_position(tails[ind + 1], tails[ind])
                tails[ind + 1] = tail

            # tail = update_tail_position(tail, head)
            history.add(tails[-1])  # the last in the list is tail-9

    print(history)
    print(len(history))


if __name__ == '__main__':
    main()









