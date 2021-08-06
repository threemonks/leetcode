##  Permutations / Combinations / Subsets:
(https://leetcode.com/problems/subsets/solution/)
Let us first review the problems of Permutations / Combinations / Subsets, since they are quite similar to each other and there are some common strategies to solve them.

First, their solution space is often quite large:

Permutations: N!.

Combinations: C_N^k = \frac{N!}{(N - k)! k!}

Subsets: 2^N, since each element could be absent or present.

Given their exponential solution space, it is tricky to ensure that the generated solutions are complete and non-redundant. It is essential to have a clear and easy-to-reason strategy.

There are generally three strategies to do it:

i) Recursion

ii) Backtracking
    See [template](../../template/algo_recursive_backtrack.py)
```
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
```

iii) Lexicographic generation based on the mapping between binary bitmasks and the corresponding permutations / combinations / subsets.
```
    []
    [[], [1]] # for each of previous result, append 1, and not append 1
    [[], [1], [2], [1, 2]] # for each of previous result, append 2, and not append 2
    ...
```

    * Backtracking
    illustration for sets:
    (https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).)
    start with empty set [], take first num 1 in nums, append to [] to get a new set [[], [1]], then recursively, take 2nd element 2, append to each, to get [[], [1], [1, 2]]
    Set (only pick element in order, i.e., don't pick 1 again after you already pick 2, as that would be permutation or combination)
```
            []
    /       |       \
  [1]      [2]       [3]
 /  \      /
[2] [3]  [3]
```
```
    dfs(nums = [1,2,3], index = 0, path = [], res = [])
    |
    |__ dfs(nums = [1,2,3], index = 1 , path = [1], res = [[]])
    |    |__ dfs(nums = [1,2,3], index = 2 , path = [1,2], res = [[],[1]])
    |    |    |__ dfs(nums = [1,2,3], index = 3, path = [1,2,3], res = [[],[1],[1,2]])
    |    |         // next: res = [[],[1],[1,2],[1,2,3]]
    |    |         // for loop will not be executed
    |    |
    |    |__ dfs(nums = [1,2,3], index = 3 , path = [1,3], res = [[],[1],[1,2],[1,2,3]])
    |    	  	   // next: res = [[],[1],[1,2],[1,2,3],[1,3]]
    |    	  	   // for loop will not be executed
    |
    |__ dfs(nums = [1,2,3], index = 2, path = [2], res = [[],[1],[1,2],[1,2,3],[1,3]])
    |    |__ dfs(nums = [1,2,3], index = 3 , path = [2,3], res = [[],[1],[1,2],[1,2,3],[1,3],[2]])
    |    	  	   // next iteration: res =  [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3]]
    |    	  	   // for loop will not be executed
    |
    |__ dfs(nums = [1,2,3], index = 3, path = [3], res =  [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3]])
                   // next iteration: res =  [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
                   // for loop will not be executed
```
    For permutation, backtrack would reuse any element that was not used, and order matters, so we could have [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
```
               [ ]
          /     |      \
       [1]     [2]     [3]
      /  \    /  \    /  \
    [2]  [3] [1] [3] [1] [2]
    |     |   |   |   |   |
    [3]  [2] [3] [1] [2] [1]
```
    For combination, order does not matter

*) generate all permutations iteratively
(an efficient algorithm for generating permutations is Johnson and Trotter algorithm https://www.geeksforgeeks.org/johnson-trotter-algorithm/)

i) A simple solution to use permutations of n-1 elements to generate permutations of n elements:

Permutations of two elements are 1 2 and 2 1.
Permutations of three elements can be obtained by inserting 3 at different positions in all permutations of size 2.
Inserting 3 in different positions of 1 2 leads to 1 2 3, 1 3 2 and 3 1 2.
Inserting 3 in different positions of 2 1 leads to 2 1 3, 2 3 1 and 3 2 1.
To generate permutations of size four, we consider all above six permutations of size three and insert 4 at different positions in every permutation.

implemented via backtracking as:
  with running partial as path, and remaining numbers nums, take first number from nums, insert into all possible positions in path, and recursive call with updated `path[:i]+[nums[0]]+path[i:]` and `nums[1:]`

Permutation Iteratively
```
"""
Iterative
取下一个可用元素，插入已有部分排列结果中每一个可能的位置，构成一个新的结果
"""
class Solution:
    def permute(self, nums):
        results = [[]]  
        for num in nums:
            newres = []
            for r in results:
                for i in range(len(r)+1):  
                    newres.append(r[:i] + [num] + r[i:])   ###insert num
            results = newres
            # results = [r[:i] + [num] + r[i:] for r in results for i in range(len(r)+1)]
        return results
```
Permute iteratively with duplicates
```
class Solution:
    def permuteUnique(self, nums):
        results = [[]]
        for num in nums:
            newres = []
            for r in results:
                for i in range(len(r)+1):
                    newres.append(r[:i]+[num]+r[i:])
                    if i<len(r) and r[i] == num:
                        break  #handles duplication
            results = newres

        return results
```

* General backtracking problems for subsets/combinations/permutations
  https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/780232/Backtracking-Python-problems%2B-solutions-interview-prep

78. Subsets: Runtime: 16 ms, faster than 96.05%
```
    class Solution(object):
        def subsets(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res = []
            self.dfs(nums, [], res)
            return res

        def dfs(nums, path, res):  # backtrack
            """
            take first element from remaining nums, append to each element in partial subset to get a new set of subsets, add this to result, and also use this as new partial subset into recursive call to next level, with nums[1:] as remaining nums to be explored (first element already processed)

            nums: remaining nums to explore/process
            path: partial subsets constructed so far after visiting leading parts of original array nums
            res: the result subsets created so far
            """
            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]], res)
```

90. Subsets II: Runtime: 20 ms, faster than 96.23%
```
    class Solution(object):
        def subsetsWithDup(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res = []
            nums.sort() # need to sort first to allow easily avoid duplicates
            self.dfs(nums, [], res)
            return res

        def dfs(self, nums, path, res):
            """
            take first element from remaining nums, append to each element in partial subset (a path from tree root ([]) to current tree node) to get a new set of subsets, add this to result, and also use this as new partial subset into recursive call to next level, with nums[1:] as remaining nums to be explored (first element already processed)

            nums: remaining nums to explore/process
            path: partial subsets (partial path from tree root ([]) to current tree node) constructed so far after visiting leading parts of original array nums
            res: the result subsets created so far
            """
            res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.dfs(nums[i+1:], path + [nums[i]], res)
```

# generate Subsets iteratively
"""
Generate subset iteratively
每次考虑一个新的元素，在考虑k-1个元素的所有结果里加上这个新的元素`nums[k]`
"""
```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]] # init to empty subset
        for i in range(n):
            # for each element is existing result, create a new result by appending new item nums[i]
            res += [r+[nums[i]] for r in res]

        return res
```

"""
subsets with dups, Iteratively

当有 n 个重复数字出现，其实就是在出现重复数字之前的所有解中，分别加 1,2,3...,n 个重复数字

"""
```
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = [[]]

        i = 0
        while i < n:
            dupcount = 0
            while i+1<n and nums[i] == nums[i+1]:
                dupcount += 1
                i += 1
            if dupcount:
                newres = []
                # for each result before duplicates, add 1,2,...dupcount copies of dup nums
                # res += [r+[nums[i]]*j for r in res for j in range(1,dupcount+2)]
                for r in res:
                    for j in range(1, dupcount+2):
                        newres.append(r+[nums[i]]*j)
                res += newres
            else:
                # add new element to each element of existing result to form new set of results
                res += [r+[nums[i]] for r in res]
            i += 1

        return res    
```