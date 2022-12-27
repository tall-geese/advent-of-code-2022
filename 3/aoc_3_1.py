
# check that each of the lines in our input has an even number of characters
# so that it can be split evenly

# They are even, but we need to remove the \n from the end.
# WE can split on this

def split_string(line: str)-> tuple[str, str]:
    """Return evenly split string if len is even, Raise ValueError otherwise."""
    z = len(line)
    if z % 2 != 0: raise ValueError
    z /= 2; z = int(z)
    return (line[:z], line[z:])

def get_priority(char: str) -> int:
    return ord(char) - 96 if char.islower() else ord(char) - 38


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')  # b/c readlines() wont get rid of the \n character

priorities = []

for line in lines:
    alpha, omega = split_string(line)
    for char in line:
        if char in alpha and char in omega: # if a single character appears in both sections
            priorities.append(get_priority(char)) # add it to our list
            break

print(priorities)
print(sum(priorities))
