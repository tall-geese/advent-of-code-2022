
from aoc_3_1 import get_priority

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')  # b/c readlines() wont get rid of the \n character

priorities = []

while lines:
    first, second, third = lines[:3]
    lines = lines[3:]
    for char in first:
        if char in second and char in third:
            priorities.append(get_priority(char))
            print(char)
            print(first, second, third)
            break

print(priorities)
print(sum(priorities))