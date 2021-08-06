"""
Sliding Window可以用两个全局pointer start_idx , end_idx 分别记录段首段尾。以start_idx=0 为起点，end_idx 向右扩张，然后在当前end_idx 为结尾的前提下（锁死window末尾)，收缩 start_idx 找到满足条件的最短window或者最长window，与全局的window最值比较。 （因为两个pointer均不会后退所以可以保证时间复杂度不超过)

"""

# [Template]

import collections


def sliding_window(s):
    if len(s) == 0:
        return ''

    longest = ''  # the global state

    # window state variables
    start_idx = 0
    window_counter = collections.Counter()

    for end_idx in range(len(str)):
        char = s[end_idx]
        window_counter[char] += 1

        # shrink window until it meets requirement
        while len(window_counter) > k:
            start_char = s[start_idx]
            window_counter[start_char] += 1
            if window_counter[start_char] == 0:
                window_counter.pop(start_char)
            start_idx += 1

        if end_idx - start_idx + 1 > len(longest):  # and meets requirement
            longest = s[start_idx:(end_idx + 1)]

    return longest