"""
    Create a directory tree from the input
    Going through each of the directories, found out which ones contain
    Files that are AT MOST 100k in size. That is the limit.
"""


# Need a function that accepts a accepts a directory name and index of our current list of file lines
    # it should return a Tuple(dir name, size of files) and also the index that we have advanced to
    # If that tuple size is less than 100k than we can add it to our collection of directories for the answer.
# Need to iterate through that position, creating a list of the file sizes that we come across

# If we hit a cd, then call the same function recursively on that directory, doing the same thing files inside.
# If we hit a cd .., then the function should return. Both the tuple and position that we advanced to.

def main():
    global small_dirs
    small_dirs = []
    import re

    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')

    a, b = gather_files('/', 1, lines)

    print(sum([i[1] for i in small_dirs]))

def gather_files(dir_name: str, ind: int, lines: list[str]) -> tuple[int, tuple[str, int]]:
    import re

    """Return name of the directory and the size of all files and subdirectories in its directory

    Parameters
    ----------
    dir_name : str
        name of the dir that passed in
    ind : int
        current index position of the lines
    lines : str 
        collection of commands and files

    Returns
    -------
    tuple[int, tuple[str, int]]
        updated index position and tuple of dir name and size
    """
    # todo: When we hit a cd .., then we should return everything


    ind = ind + 1  # skip over the 'cd [dirname]'
    files = []

    while ind < len(lines):
        line = lines[ind]
        ind += 1

        if line.startswith('$ ls'): # should be the first thing we encounter 
            continue  
        elif line.startswith('dir'):
            sub_dir = re.search('dir (\w+)', line).group(1)
            files.append(sub_dir)
        elif line.startswith('$ cd ..'):  # Return this function
            return ind, (dir_name, sum(files))
        elif line.startswith('$ cd '):
            sub_dir = re.search('cd (\w+)', line).group(1)
            move_ind, dir_stats = gather_files(sub_dir, ind, lines)

            if dir_stats[1] <= 100000:  # if small enough, add to our global list of small dirs
                small_dirs.append(dir_stats)

            ind = move_ind
            files[files.index(sub_dir)] = dir_stats[1]  # replace sub_dir name with its size

        else:  # otherwise its a normal file
            file_size = re.search('^(\d+)?\s', line).group(1)
            files.append(int(file_size))

    
    # Otherwise we should be at the end of the file
    print('stop here???/')
    return ind, (dir_name, sum(files))


if __name__ == '__main__':
    main()





