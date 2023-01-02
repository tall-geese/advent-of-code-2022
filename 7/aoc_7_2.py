"""
    This time we are going through and listing the size of the all the directories
    We are trying to find the smallest directory that, if deleted,
    would free up enough space for the 30,000,000 update
    assuming the that total disk size is 70,000,000

"""


def main():
    global all_dirs
    global free_space
    all_dirs = []
    import re

    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')

    _, dir_stats = gather_files('/', 1, lines)
    all_dirs.append(('/', dir_stats[1]))


    # Now calc the difference and how to iterate though each of the dirs to find the smalles possible difference
    free_space = 70E6 - dir_stats[1]
    needed_space = 30E6 - free_space
    all_dirs = list(filter(lambda x: x[1] >= needed_space, all_dirs))  # comment this in and out to test
    all_dirs.sort(key=lambda x: x[1])

    print(f'free_space - {free_space:,}')
    print(f'needed space - {needed_space:,}')
    for dir in all_dirs:
        print(f'\t{dir[0]} - {dir[1]:,}')



def calc_size_diff(file: tuple[str, int]):
    pass

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

            # if dir_stats[1] <= 100000:  # if small enough, add to our global list of small dirs
            all_dirs.append(dir_stats)

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





