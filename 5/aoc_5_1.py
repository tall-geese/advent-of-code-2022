
# Start by extracting alkl of the information from the first 9 columns
# and arranging them into a list of lists

import re
# [\[(\D)\]]?\s*?
pattern = '^' + r'(\[\D\]|\s{3})\s' * 9
pattern = pattern[:-2]
firstLine = True

for line in open('input2.txt', 'r'):
    print(re.search(pattern, line).groups())