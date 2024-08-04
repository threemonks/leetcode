##  Recursive/Backtracking problems
https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1186/lectures/10-RecursiveBacktracking2/10-RecursiveBacktracking2.pdf


###  Common Problem Types for Recursive Backtracking• Partitionable (determine whether a solution exists)
• Knapsack Problem (find the best solution)
• Maze Solving (find a solution)
• Clumsy Thumbsy (find all solutions)

###  Determine whether a solution exists• Find a solution
• Find the best solution
• Count the number of solutions
• Print/find all the solutions

			        Exhaustive Search		True Backtrack
                    (try everything)        (once you find a valid solution, stop that branch or return)
Permutations		printAllBinary			escapeMaze
			        totalSum			    8 Queens
							                crack password

Combinations/Subsets	sublist				canCalculateSum


##  Backtracking Template
In this article, we will present you a pseudocode template that summarizes some common patterns for the backtracking algorithms. Furthermore, we will demonstrate with some concrete examples on how to apply the template.

- Template
With the N-queen example as we presented in the previous article, one might have noticed some patterns about the backtracking algorithm. In the following, we present you a pseudocode template, which could help you to clarify the idea and structure the code when implementing the backtracking algorithms.

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)

Here are a few notes about the above pseudocode.

Overall, the enumeration of candidates is done in two levels: 1). at the first level, the function is implemented as recursion. At each occurrence of recursion, the function is one step further to the final solution.  2). as the second level, within the recursion, we have an iteration that allows us to explore all the candidates that are of the same progress to the final solution.

The backtracking should happen at the level of the iteration within the recursion.

Unlike brute-force search, in backtracking algorithms we are often able to determine if a partial solution candidate is worth exploring further (i.e. is_valid(next_candidate)), which allows us to prune the search zones. This is also known as the constraint, e.g. the attacking zone of queen in N-queen game.

There are two symmetric functions that allow us to mark the decision (place(candidate)) and revert the decision (remove(candidate)).

"""
Recursive backtracking
"""
def solve(config):
    if no more choices: # BASE CASE
        return conf is goal_state
    for all available choices:
            try one choice c
            # recursively solve after making choice
            ok = solve(conf with choice c made)
            if ok:
                return True
            else:
                unmake choice c
                return False

    return False # tried all choices, no solution found

"""
8 Queens strategy
"""
Start in the leftmost columm
If all queens are placed, return true
for (every possible choice among the rows in this column)
 if the queen can be placed safely there,
make that choice and then recursively try to place the rest of the queens
if recursion successful, return true
if !successful, remove queen and try another row in this column
if all rows have been tried and nothing worked, return false to trigger backtracking

"""
solve sudoku
"""
Find row, col of an unassigned cell
If there is none, return true
For digits from 1 to 9
 if there is no conflict for digit at row,col
assign digit to row,col and recursively try fill in rest of grid
if recursion successful, return true
if !successful, remove digit and try another
if all digits have been tried and nothing worked, return false to trigger backtracking

"""
Solving cryptarithmetic puzzles
"""
First, create a list of all the characters that need assigning to pass to Solve
If all characters are assigned, return true if puzzle is solved, false otherwise
Otherwise, consider the first unassigned character
for (every possible choice among the digits not in use)
make that choice and then recursively try to assign the rest of the characters
if recursion sucessful, return true
if !successful, unmake assignment and try another digit
if all digits have been tried and nothing worked, return false to trigger backtracking

"""
cryptarithmetic puzzle with early pruning
"""

Start by examining the rightmost digit of the topmost row, with a carry of 0
If we are beyond the leftmost digit of the puzzle, return true if no carry, false otherwise
If we are currently trying to assign a char in one of the addends
If char already assigned, just recur on row beneath this one, adding value into sum
If not assigned, then
 for (every possible choice among the digits not in use)
 make that choice and then on row beneath this one, if successful, return true
if !successful, unmake assignment and try another digit
return false if no assignment worked to trigger backtracking
Else if trying to assign a char in the sum
If char assigned & matches correct,
 recur on next column to the left with carry, if success return true
If char assigned & doesn't match, return false
If char unassigned & correct digit already used, return false
If char unassigned & correct digit unused,
 assign it and recur on next column to left with carry, if success return true
 return false to trigger backtracking




