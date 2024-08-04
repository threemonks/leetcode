"""

input word list
abe ada cage cat dog

randonly generate 10 words that have
1. same distribution of the starting character as input list's first char
2. any character following certain character should follow same distribution as those characters have in the input that follows the same char
e.g., in input, we have {'a': {'b':1, 'd':1, 'g': 1, 't': 1}}, so in the generatd string, should have same distribution
3. ending character should also have same distribution, and words end when last char is one of the ending chars in input string

"""