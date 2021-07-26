"""
1371. Find the Longest Substring Containing Vowels in Even Counts
Medium

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.



Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.


Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.

"""
"""
String bitmask

use an integer of 5 bits, each bit represents whether given vowel {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4} has appeared even (0) or odd (1) number of times so far
while scanning through the string, we will use XOR operation to update this number to represent current pattern (odd/even occurrences of each vowels), we store the first appearance of each pattern of occurrences of vowels (i), if we later find the same pattern at index j, then we know all vowels must appear even number of times between the first occurrence and this one, as XOR operation on same bit twice would return it to its original state, and the distance between these two index (j-i) is the current max length of substring with each vowels appearing even number of times. We can keep update the max size of substring as we scan through the string. The final result would be the max size of such substring.

Why do we need to init first_pos = {0: -1}
-1 stands for the empty (sub)string and 0 stands for the appeared times of "aeiou" are all even (to be specific, all zero indeed). To be clarified, -1 is needed as when we calculate the substring length: i - (-1) = i + 1 which means length of the substring from 0 to i included is i+1.

quoted from this post
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531850/Python-solution-in-O(n)-time-and-O(1)-space-explained
We can use 5 bits to represent the parity of the number of occurrences of vowels. For example, we can use 0/1 for even/odd numbers, then if we have a:0, e:1, i:2, o:3, u:4, the representation would be 01010. As we scan through the array, we can update the representation in O(1) time by using the XOR operation, and then store the index where every different representation first appeared. When we encounter a representation, say 01010 again at index j, we can look back on the index i where 01010 first appeared, and we know that the substring from i to j must be a valid string, and it is the longest valid substring that ends at j

time O(N)
space O(1) ~ 2**5

"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        first_pos = {
            0: -1}  # first index of given pattern (a pattern represents even or odd count state of all five vowels, one bit for each)
        cur = 0  # current pattern (each bit represents number of times (odd or even) that given vowel has appeared so far)
        res = 0
        for i, c in enumerate(s):
            if c in vowels:
                v = vowels[c]
                cur ^= (2 ** v)
            if cur in first_pos:
                res = max(res, i - first_pos[cur])
            else:
                first_pos[cur] = i
            # print('i=%s c=%s cur=%s res=%s first_pos=%s' % (i, c, bin(cur), res, str(first_pos)))

        return res


"""
Hash Table

Use a boolean vector (1-d array) of length 5 (len('aeiou')) to store whether we see even number times of this vowel or not, keep an array of this vector as we traverse the string. If see the same vector again later, we found a window that gives even counts of all vowels. Keep the max of such window size as we iterate.


time complexity: O(N*5)=O(N)

follow up: can use bitmask to represent evenness of all five vowels at each index using one number, this will improve speed (though not time complexity)
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        prefix_evens = []
        evens = [True for _ in range(5)]  # do we see even counts of given vowel so far
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}  # vowel index in counts

        # first index of each vector, i.e., the best left boundary that could give us longest valid substring for this vector
        seen = {(True, True, True, True, True): -1}  # all True is sentinel value

        ans = 0
        for i, c in enumerate(s):
            if c in vowels:
                evens[vowels[c]] = not evens[vowels[c]]
            # now store this vector into array prefix_evens
            evens_tuple = tuple(evens)
            prefix_evens.append(evens_tuple)
            # print('i=%s tuple=%s prev index=%s' % (i, evens_tuple, seen.get(evens_tuple)))
            if evens_tuple not in seen:
                # mark first index of this evens vector
                seen[evens_tuple] = i
            else:
                # one valid window with all vowels have even counts, update ans if possible
                ans = max(ans, i - seen[evens_tuple])

        return ans


def main():
    sol = Solution()
    assert sol.findTheLongestSubstring("eleetminicoworoep") == 13, 'fails'

    assert sol.findTheLongestSubstring("leetcodeisgreat") == 5, 'fails'

    assert sol.findTheLongestSubstring("bcbcbc") == 6, 'fails'

if __name__ == '__main__':
   main()