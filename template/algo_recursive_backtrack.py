"""
recursive function template
"""

def myfunc(n, **kwargs):
    # base case
    if n == 0:
        return
    # recursive call to myself
    else:
        myfunc(n-1)

"""
backtrack template
"""
def backtrack(choices, chosen):
    # base case
    if not choices:
        print(chosen)
        return

    # recursive case
    # choose current element choices[0]
    chosen.append(choices[0])
    # explore
    backtrack(choices[1:], chosen)
    # unchoose current element choices[0]
    chosen.pop()

"""
Knapsack problem / backtrack
"""
def fill_knapsack(objects, weight, best_score):
    if weight < 0: # too many objects
        return 0
    local_best_score = best_score
    for i, obj in enumerate(objects):
        curr_value = best_score + obj.value
        curr_weight = weight + obj.weight

        # remove current obj

        # recursive exploration with current obj removed
        curr_value = fill_knapsack(objects[:i]+objects[i+1:], curr_weight, curr_value)
        if local_best_score < curr_value:
            local_best_score = curr_value
        # restore current obj

    return local_best_score

"""
walk maze

start marked with 'S', finish marked with 'F', wall marked with 'X'

approach:
1. mark position seen with period '.', mark backtracking with 'b'
2. have a case for all valid inputs
3. must have base cases
4. make forward progress toward the base case
"""
def solve_maze(row, col, grid):
    # base case
    # if wall
    if (grid[row][col] == 'X'):
        return False
    # if visited
    if (grid[row][col] == '.'):
        return False
    # if finish
    if (grid[row][col] == '.'):
        return True

    # mark visited
    grid[row][col] == '.'

    # recusrively call solve_maze(row, col, grid) for all directions,
    # if any direction returns True, we return True
    if solve_maze(row-1, col, grid):
        return True

    if solve_maze(row, col+1, grid):
        return True

    if solve_maze(row+1, col, grid):
        return True

    if solve_maze(row, col-1, grid):
        return True

    # no direction is successful
    # mark as backtrack
    grid[row][col] == 'b'
    return False

"""
Classic exhaustive permutation pattern

pseudo code:
    If you have no more characters left to rearrange, print current permutation
    for (every possible choice among the characters left to rearrange):
        Make a choice and add that character to the permutation so far
        Use recursion to rearrange the remaining letters
"""
def recursive_permute(sofar, rest):
    if not rest:
        print(sofar)
    else:
        for i in range(len(rest)):
            recursive_permute(sofar + rest[i], rest[:i]+rest[i+1:])


"""
Classic exhaustive subset pattern

    If there are no more elements remaining,
        print current subset
    else
        Consider the next element of those remaining
        Try adding it to the current subset, and use recursion to build subsets from here
        Try not adding it to current subset, and use recursion to build subsets from here

"""
def recursive_subsets(sofar, rest):
    if not rest:
        print(sofar)
    else:
        # include first char
        recursive_subsets(sofar + rest[0], rest[1:])
        # exclude first char
        recursive_subsets(sofar, rest[1:])

