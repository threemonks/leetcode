### cache/memoization
from functools import lru_cache
lru_cache(None)

### transpose 2-d array (swap columns and rows)
    array2d=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    zip(*array2d)

import collections
counter = collections.Counter(iterable)
sorted_counter_by_freq = sorted([(item, count) item, count in counter.items()], lambda x: x[1])

dct_of_int = collections.defaultdict(int)
dct_of_int[key] += 1

dct_of_list = collections.defaultdict(list)
dct_of_list[key].append(new_val)

### modulo
    15 % 4 => 3
    8 % -3 => -1
    37 // 5 => 7
    37 % 5 => 2
    num % 2 == 0 => check is even

### nested list comprehension and for loops

    #!python
    # The list comprehension said:
      [ expression
        for line in open('arecibo.txt')
        for char in line.strip() ]

    # It therefore meant:
    for line in open('arecibo.txt'):
        for char in line.strip():
            list.append(expression)

### multiple variable (tuple) assignment:

    slow, slow.next, rev = slow.next, rev, slow
    
    expressions on the right side are evaluated before any of the assignments, and then they are assigned one by one, from left to right.
    That first evaluates the right side and then assigns to the left side from left to right. So first, slow becomes what used to be slow.next. And then, slow.next gets assigned something, but that slow is already changed!
    
    or can be written as:
    temp1 = slow
    temp2 = rev
    temp3 = slow.next
    rev = temp1
    rev.next = temp2
    slow = temp3