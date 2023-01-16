"""


Psuedo
--------
We can continually multiple the number by 0.1
until it is within a rnage of >50 and < 100
or something like that and then performthe modulus operation.

This is hoping that the multiplication is not an expensive operation
in programming


Guessed
----------
14400720009 - too low
14400359996 - too low
21800916620 - good

"""

from monkeys2 import monkey_json, lcm
import math

def main():
    # round = 0

    # Set all of the monkeys as having 0 inspections so far...
    for monkey in monkey_json:
        monkey.update({'inspections': 0})

    for i in range(10000):
        for ind, monkey in enumerate(monkey_json):
            for item in monkey['items']:
                monkey['inspections'] += 1
                item = monkey['operation'](item)
                item = item % lcm
                # if item >= 200 and item % 10 == 0:
                #     item /= 10
                # item = math.floor(item / 3)
                monkey_json[monkey['test'](item)]['items'].append(item)

                monkey['items'] = []
            # After this, set it as having no items, we threw them all

    scores = [(ind, monkey['inspections']) for ind, monkey in enumerate(monkey_json)]
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(monkey_json)

    # Print out the multiplied inspections of the two monkeys
    # with the highest inspections
    print('*****   Level of Monkey Business   ***** ')
    print(scores[0][1] * scores[1][1])




if __name__ == "__main__":
    main()