"""
1152. Analyze User Website Visit Pattern
Medium

200

1839

Add to List

Share
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.



Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation:
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.


Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.

"""
from collections import defaultdict
from typing import List

"""
Hash Table / Sorting

group by user
sort by timestamp, use timestamp index to get websites, accumulate 3-tuple websites visit count for each user, then return the one with max count (and smaller lexicographical order if multiple such sequence with same max count)

mistakes:
1. 3-seq could be non-consecutive 
2. count # of users who visited those 3-seq, not just how many times the 3-seq got visited
"""


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        uw = defaultdict(list)
        timestamp = sorted([(ts, i) for i, ts in enumerate(timestamp)])

        for ts, i in timestamp:
            # print('%s %s %s' % (username[i], ts, website[i]))
            u = username[i]
            w = website[i]
            uw[u].append(w)

        counter = defaultdict(set)
        for key, val in uw.items():
            # print('key=%s val=%s' % (key, val))
            vlen = len(val)
            if vlen >= 3:
                for i in range(0, vlen):
                    for j in range(i + 1, vlen):
                        for k in range(j + 1, vlen):
                            pattern = [val[i]] + [val[j]] + [val[k]]
                            vkey = tuple(pattern)
                            counter[vkey].add(key)

        # print(counter)

        max_count, max_seq = 0, None
        for seq, users in counter.items():
            if len(users) > max_count:
                max_count = len(users)
                max_seq = seq
            elif len(users) == max_count and max_seq > seq:
                max_seq = seq

        return list(max_seq)


def main():
    sol = Solution()
    assert sol.mostVisitedPattern(username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]) == ["home","about","career"], 'fails'

    # assert sol.mostVisitedPattern(username = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"], timestamp = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930], website = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]) == ["hibympufi","hibympufi","yljmntrclw"], 'fails'

if __name__ == '__main__':
   main()