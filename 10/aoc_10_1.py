
"""
Need to find out the signal strenght at certain intervals  (value  * cycle count)
    20, 60, 100, 140, ... 220  and then return the sum of those 

Only two instruciton tpyes thta need to be handled
    noop - takes one cycle and does nothing 
    addx V - takes two cycles to complete. After completing, adds the value V to the current value

When we say we are looking for a value during a cycle number, its the number at the beginning of that cylce
even if we're in phase 2 of adding a nunmber, we return the value as it was at the beginning of that step
and actually add the number at the end of the step

Psuedo
---------



Tests
-----
do the split and make sure that we are getting a negative number

Guesses 
---------
13280 - too high
11960 --good

"""

def get_signal(value: int, cycle: int) -> int:
    return value * cycle

# def 


def main():
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')

    print(lines)

    cycle = 0
    value = 1
    ind = 0
    reserve_val = 0
    signal_scores = []

    # While loop will help us perform on the same line twice, make this all simpler
    
    while (ind + 1) < len(lines):
        cycle += 1

        # Something here to check signal if in the necessary step
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_scores.append(get_signal(value, cycle))
        

        # TODO: something here to check a reserve value
            # Then set it back to 0
        if reserve_val != 0:
            value += reserve_val
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

    print(signal_scores)
    print(sum(signal_scores))


if __name__ == '__main__':
    main()


