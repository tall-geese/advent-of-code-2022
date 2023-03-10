"""

Monkeys start with a list of a items that have a integer value indicating the worrieness level.
When inspecting an item, monkey will peform the Operation, usually increaing the worry level
After each monkey performs the operation on an item, but before testing...
    divide the worriness by 3 and math.floor() it

Then the monkey runs a test on an item
It will throw to another monkey in which case
that item is appended onto the end of the list for that monkey

In each round we iterate through each monkey
which iterates through each item that it has on hand, before moving
to the next monkey once its out of items


Count the total number of times each monkey inspected an item over 20 rounds.
Multiply the score of the two highest monkeys together to ge the "level"

What is the level of monkey business AFTER 20 rounds of stuff-slinging simian shenanigans?
"""

from monkeys import monkey_json
import math

def main():
    # round = 0

    # Set all of the monkeys as having 0 inspections so far...
    for monkey in monkey_json:
        monkey.update({'inspections': 0})

    for i in range(20):
        for ind, monkey in enumerate(monkey_json):
            for item in monkey['items']:
                monkey['inspections'] += 1
                item = monkey['operation'](item)
                item = math.floor(item / 3)
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