
"""
Tracking where the position of a sprite is when drawing the pixel of a row
while iterating through the cylces

Sprite is 3 pixels wide
Each cycle works like this
    begin executing a command
    draw the crt pixel
    finish executing the command (update a position if appropriate)

First row is from cycle 1 to 40
then next is 41 to 80 and so on in that order
until we hit the last cycle of 240

We actually need to print out the rows, so hold onto them as we draw chcaracters onto them

Print them all out once finished, what are the 8 capital letters appearing on the screen

Does the sprite reset its position when we move to a new row??

Psuedo
---------



Guesses 
---------
EJCFPGLH
"""

import math

def get_pixel_shape(ind: int, sprite_position: int) -> str:
    cond = (ind == sprite_position or (ind - 1) == sprite_position or (ind + 1) == sprite_position)
    return '#' if cond else '.'

def main():
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')

    print(lines)

    cycle = 0
    sprite_pos = 1
    crt_rows = [[] for i in range(6)]
    reserve_val = 0
    ind = 0
    crt_latest = 0
    # value = 1
    # signal_scores = []

    # While loop will help us perform on the same line twice, make this all simpler
    
    while (ind + 1) < len(lines) and cycle < 241:
        cycle += 1

        # Grab the row that we are going to update, must be from 0 - 5
        crt_row_ind = math.floor((cycle - 1) / 40)
        crt_row = crt_rows[crt_row_ind]

        # If we moved to a new CRT row, reset the sprite position
        # if crt_row > crt_latest:
        #     crt_latest = crt_row
        #     sprite_pos = 0

        # Find the position in that row that we are going to update, must be 0 - 39
        x_pos = (cycle - 1) % 40

        # Draw the pixel, based on the current position of the sprite
        # crt_row.append(get_pixel_shape(x_pos, sprite_pos))
        crt_row.insert(x_pos, get_pixel_shape(x_pos, sprite_pos))

        # Check a reserve value
            # Then set it back to 0
        if reserve_val != 0:
            sprite_pos += reserve_val
            reserve_val = 0
        else:
        # Otherwise perform an operation, optionally setting the ind back if we need to repeat a line
            if lines[ind].startswith('noop'):
                pass
            else:
                add_val = lines[ind].split(' ')[1]
                reserve_val = int(add_val)
                continue

        ind += 1

    with open('out.txt', 'w') as outfile:
        for row in crt_rows:
            outfile.writelines(row)
            outfile.write('\n')


if __name__ == '__main__':
    main()


