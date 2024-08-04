"""
[[1, 5], [7, 10], [8, 12], [2, 6]] covers 10 units.

Visualization:
  _____       _____
 |     |     |     |
 |     |    _|__   |
 |  ___|_  | |  |  |
_|_|___|_|_|_|__|__|__
 1 2   5 6 7 8  10 12

 [[1, 5], [2, 6], [7, 10], [8, 12]]

 sort -> O(Nlog(N)) N = len(intervals)
 space O(N)
"""


def get_covered_length(intervals):
    intervals = sorted(intervals)

    merged = []  # list of non-overlapping merged intervals

    for intv in intervals:
        if len(merged) > 0 and merged[-1][1] > intv[0]:
            merged[-1][1] = max(merged[-1][1], intv[1])  # [[1, 6]]
        else:
            merged.extend([intv])  # [[1, 6], [7, 12]]

    ans = 0
    for intv in merged:  # [[1, 6], [7, 12]]
        ans += intv[1] - intv[0]

    return ans


# intervals = [[1, 5], [7, 10], [8, 12], [2, 6]]
# print(get_covered_length(intervals))
# # assert get_covered_length(intervals) == 10, 'fails'
# print(get_covered_length([]))
# intervals = [[1, 5]]
# print(get_covered_length(intervals))

intervals = [[1, 7], [8, 10], [9, 12], [2, 6]]
print(get_covered_length(intervals))
