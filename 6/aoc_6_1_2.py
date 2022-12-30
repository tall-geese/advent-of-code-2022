
"""
Iterate through our input until we find the first sequence of
unique 4 [or 14 for the second example] characters in a row. Then report back the position + 1
becuase it is one-indexed

"""

from collections import deque


marker = deque(maxlen=14)

# How to compare all of the characters in our list?
with open('input.txt', 'r') as file:
    input = file.read()

for ind, char in enumerate(input):
    marker.append(char)
    if len(marker) == len(set(marker)) and len(marker) == 14: 
        break
else:
    print('Didnt find the marker')
    quit()

print(ind)
print(marker)