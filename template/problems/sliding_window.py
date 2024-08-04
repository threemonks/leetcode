"""
Sliding Window可以用两个全局pointer start_idx , end_idx 分别记录段首段尾。以start_idx=0 为起点，end_idx 向右扩张，然后在当前end_idx 为结尾的前提下（锁死window末尾)，收缩 start_idx 找到满足条件的最短window或者最长window，与全局的window最值比较。 （因为两个pointer均不会后退所以可以保证时间复杂度不超过)

"""

# [Template]

import collections


def sliding_window(s, k):
    """
    longest substring with at most k disinct chars

    :param s:
    :param k: max window size
    :return:
    """
    n = len(s)

    if n == 0:
        return ''
    counts = collections.defaultdict(int)
    left, right = 0, 0

    while right < n:
        counts[s[right]] += 1
        while len(counts.keys()) < k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0: # drop keys for chars with 0 counts
                del counts[s[left]]
            left += 1
        right += 1

    return max(counts.values())