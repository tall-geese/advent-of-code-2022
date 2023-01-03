
"""
    How many trees are visible in the arrangement?


    All trees on the first and last row are visible
    All trees at the beginning and end of each row are visible

    Trees on the interior are visible only if
        every other tree to the top, left, right or bottom
        are all SHORTER than it.
    If another tree is the same height, then its considered to hide 
        the interior tree

    Tips
    --------
    access a col like df[0] for the first column
    access a row like df.loc[0] for the first row

    iter over ind, Series of a df using df.iterrows()
    iter over the ind, val of a Series with s.items()

    Psuedo
    ----
    Start by dropping the first and last rows of the df.
    We can just add 2x 99 to the final count, becuase these are all visible

    Iterate through each of the interior rows
    its position in the row is the same as the column that its in

    if the col_ind == 0 or col_ind ==  98 then its an outside one, add to list
    Otherwise grab the slice on both side adn turn them into numpy arrays
        if our value is greater than the .max() of either, then add visibility, dont need to check the other

    if the row_ind == 0 or row_ind == 98 then its an outside, add for visibility
        otherwise grab the entire col and slice at the index, turning into numpy array
        if its greater than the .max() in either direction, add +1 visibility, dont bother checking the other

    


"""

import pandas as pd
import numpy as np

def changeto_csv():
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')

    output = [','.join(line) for line in lines]

    with open('input.csv', 'w') as file:
        file.write('\n'.join(output))



def main():


    df = pd.read_csv('input.csv', header=None)
    # print(len(df.loc[0]))

    visible_trees = 0

    for row_ind, row in df.iterrows():
        if row_ind == 0 or row_ind == 98:  # If its on the top or bottom of the grid
            visible_trees += 99
            continue
        for col_ind, val in row.items():
            if col_ind == 0 or col_ind == 98:  # If its on the left or right side
                visible_trees += 1
            else:
                # Have to create lists of the items on each direction, stop when we find one
                if (
                    side_visible(val, np.array(row[:col_ind]))   # left side
                    or side_visible(val, np.array(row[col_ind + 1:])) # right side
                    or side_visible(val, np.array(df[col_ind][:row_ind]))   # top side
                    or side_visible(val, np.array(df[col_ind][row_ind + 1:]))  # bottom side
                ):
                    visible_trees += 1
                
    print(visible_trees)

def side_visible(tree: int, others: np.ndarray) -> bool:
    return tree > others.max()


if __name__ ==  '__main__':
    main()



