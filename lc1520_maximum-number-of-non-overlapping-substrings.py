"""
1520. Maximum Number of Non-Overlapping Substrings
Hard

349

47

Add to List

Share
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.



Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.


Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
"""
from typing import List

"""
Greedy

thoughts:
1. no overlap in any two valid substring, unless one is inside another
1.1 but if one valid substring is within another, since we only need to find total count of shortest valid substring, we can discard the longer substring that contains another valid substring, and only keep the one being contained
2. only the start of a letter can be start of a valid substring, so we check each of such start, find the smallest end that would form a valid substring 
3. then the problem becomes interval scheduling maximization

steps:
1. for all valid starts (start of each char), find longest valid substring (if the longest extended to left as well due to some letter inbetween has even ealier start, then this start does not provide a valid substring)
2. now we need to find maximum scheduling without interval overlap (schedule conflict)
2.1 The problem now becomes an interval scheduling maximization problem (ISMP) (https://en.wikipedia.org/wiki/Interval_scheduling).
We can solve this in O(n) time by greedily taking the next non-overlapping substring with the left-most endpoint.

Interval Scheduling Maximization:
Greedy polynomial solution
The following greedy algorithm does find the optimal solution:
Select the interval, x, with the earliest finishing time (if two with same ending, pick smaller starting first)
Remove x, and all intervals intersecting x, from the set of candidate intervals.
Repeat until the set of candidate intervals is empty.

mistakes:
1. for letter occurs once, its start is also its end
2. need to use dict to store start and end of each letter's interval/substring, and extend as necessary (letters inbetween needs to be completely included in the substring)
3. need to get maximum number of intervals without overlapping
4. to maximize schedule greedily, we need to sort by smallest ending time first (and also sort by start time smaller first if same ending time)
5. for maximize scheduling, only consider next interval if its start does not overlap with previous ending
"""


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        starts = {c: i for i, c in reversed(list(enumerate(s)))}
        ends = {c: i for i, c in enumerate(s)}

        intervals = []
        for c in set(s):
            # update ending to max of ending of all characters in between
            start = starts[c]
            end = ends[c]
            i = start
            while i <= end and start == starts[c]:
                start = min(start, starts[s[i]])
                end = max(end, ends[s[i]])
                i += 1
            if start == starts[c]:  # didn't expand to left, so we got a valid substring starts at start
                intervals.append((start, end))

        intervals.sort(key=lambda x: (x[1], x[0]))  # sort by end first, then start

        # maximum interval scheduling, greedily take the next one with smallest ending time,
        # if its start does not overlap with previous ending
        res, prev_end = [], -1
        for start, end in intervals:
            if start > prev_end:  # next smallest ending interval's start does not overlap with previous ending
                res.append(s[start:end + 1])  # add to result
                prev_end = end  # update previous ending

        return res

def main():
    sol = Solution()
    assert sol.maxNumOfSubstrings(s = "adefaddaccc") == ["e","f","ccc"], 'fails'

    assert sol.maxNumOfSubstrings(s = "abbaccd") == ["bb","cc", "d"], 'fails'

    assert sol.maxNumOfSubstrings(s = "cbadabdb") == ["c","badabdb"], 'fails'

if __name__ == '__main__':
   main()