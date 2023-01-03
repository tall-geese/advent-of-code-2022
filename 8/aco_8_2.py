
"""
    What is the hightest scenic score possible?

    for the trees that are tree-locked,
    count the number of trees out that they are able to view.
    can see up to and including the tallest tree blocking the view
    of the other trees behind

    Tips
    --------
    access a col like df[0] for the first column
    access a row like df.loc[0] for the first row

    iter over ind, Series of a df using df.iterrows()
    iter over the ind, val of a Series with s.items()

    Psuedo
    ----
    if we have a tree that is of the outer edge, just continue to the next iteration

    otherwise need a function to calculate scenic score givem the tree height
    and a list of the trees proceeding in the given direction.
    
    start with init value of 0 and iterate throught the list,
    incrementing each time we find a smaller tree
    increment one last time when find a tree the same height or higher,
    then return the score.

    multiply these scores together to get the scenic view.
    Keep track of the highest and its position on the grid
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

    highest_score = 0
    score_position = None

    for row_ind, row in df.iterrows():
        if row_ind == 0 or row_ind == 98:  # If its on the top or bottom of the grid
            continue  # dont bother with these guys
        for col_ind, val in row.items():
            if col_ind == 0 or col_ind == 98:  # If its on the left or right side
                continue  # dont bother with edge trees
            else:
                # Have to create lists of the items on each direction, stop when we find one
                left = get_view_score(val, np.array(row[:col_ind][::-1]))   # left side - must reverse
                right =  get_view_score(val, np.array(row[col_ind + 1:])) # right side
                top = get_view_score(val, np.array(df[col_ind][:row_ind][::-1]))   # top side - must reverse
                bottom = get_view_score(val, np.array(df[col_ind][row_ind + 1:]))  # bottom side
                
                view_score = left * right * top * bottom
                if view_score > highest_score:
                    print(val)
                    highest_score = view_score
                    score_position = (row_ind, col_ind)

    print(highest_score)
    print(score_position)

def get_view_score(tree: int, others: np.ndarray) -> int:
    """return the view score of the tree, between [0, len(others)]

    Parameters
    ----------
    tree : int
        height of the tree in question
    others : np.ndarray
        list of tree heights in one direction, in order from 
        adjactent -> furtherst out

    Returns
    -------
    int
        the amount of trees in view that direction, including the tallest one
        obstructing others behind it
    """    

    score: int = 0
    for neighbor in others:
        score += 1
        if neighbor >= tree: break
    return score

if __name__ ==  '__main__':
    main()



