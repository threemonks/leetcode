"""
1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number
Medium

57

13

Add to List

Share
You are given a string num, representing a large integer, and an integer k.

We call some integer wonderful if it is a permutation of the digits in num and is greater in value than num. There can be many wonderful integers. However, we only care about the smallest-valued ones.

For example, when num = "5489355142":
The 1st smallest wonderful integer is "5489355214".
The 2nd smallest wonderful integer is "5489355241".
The 3rd smallest wonderful integer is "5489355412".
The 4th smallest wonderful integer is "5489355421".
Return the minimum number of adjacent digit swaps that needs to be applied to num to reach the kth smallest wonderful integer.

The tests are generated in such a way that kth smallest wonderful integer exists.



Example 1:

Input: num = "5489355142", k = 4
Output: 2
Explanation: The 4th smallest wonderful number is "5489355421". To get this number:
- Swap index 7 with index 8: "5489355142" -> "5489355412"
- Swap index 8 with index 9: "5489355412" -> "5489355421"
Example 2:

Input: num = "11112", k = 4
Output: 4
Explanation: The 4th smallest wonderful number is "21111". To get this number:
- Swap index 3 with index 4: "11112" -> "11121"
- Swap index 2 with index 3: "11121" -> "11211"
- Swap index 1 with index 2: "11211" -> "12111"
- Swap index 0 with index 1: "12111" -> "21111"
Example 3:

Input: num = "00123", k = 1
Output: 1
Explanation: The 1st smallest wonderful number is "00132". To get this number:
- Swap index 3 with index 4: "00123" -> "00132"


Constraints:

2 <= num.length <= 1000
1 <= k <= 1000
num only consists of digits.
"""
"""
Greedy

1. find next permutation of given string k times
    1. 从右边开始找到第一个不符合递增的数字nums[i]，from right end, first nums[i]<nums[i+1]
       如果找不到，则整个数组是降序，没有next permutation，直接整个数组反序
    2. 从右边开始找到大于nums[i]但是尽可能小的数字nums[j]，就是从右边第一个大于nums[i]的数字，因为该段子数组是从右往左递增
    3. 交换这两个数字，swap nums[i] and nums[j]
    4. 把i+1到数组右端后缀子数组反序, reverse nums[i+1:]
2. find min number of adjacent swaps required to change new string back to original
    相邻元素交换得到原数组的次数等于逆序对数
    # count min number of swaps required to make new string to original
    1. 遍历num，index i, j=i
    2. 对于每一个i，如果两数组对应位置相同，nums[i]==nums1[j], i += 1
    3. 如果num[i]和num1[j]不等，nums[i] != nums1[j], 把指针j右移，j += 1，直到找到nums[i] == nums1[j]
    4. while i<j， 相邻两数交换nums1[j-1]，nums1[j]，计数， ans+=1, j-=1
    We can find the number of swaps (min) required to make original == new_string (Refer code below)

    5489355142 vs 5489355421

    i is pointing at '1' and j is pointing at '4', because s1[i] != s2[j].
    We do j++ till they match, which bring j to '1' in s2 : 5489355421

    now, we start swapping from j to i and get following results -

    5489355421 (swap 1 with 2) : 5489355412 --> j is at 1
    i!=j
    so swap again;
    5489355412 (swap 1 with 2) : 5489355142 --> j is at 1
    i==j, so stop.

    Do the same for rest of the string. No of swaps = No of steps required to make them equal.

mistakes:
1. call next_perm on result for k times
"""


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        n = len(num)

        def next_perm(s: list) -> list:
            # 1. from right, find first decreasing char
            i = n - 2
            while i >= 0 and s[i] >= s[i + 1]:
                i -= 1
            # print('first decreasing char index %s s[i]=%s' % (i, s[i]))
            # 2. from right, find first character that's larger than i
            j = n - 1
            while j >= i and s[j] <= s[i]:
                j -= 1
            # print('first char larger than i %s s[j]=%s' % (j, s[j]))
            # 3. swap s[i] and ss[j]
            s[i], s[j] = s[j], s[i]
            # print('after swap i=%s and j=%s %s' % (i, j, s))

            # 4. reverse s[i+1:], when entire array is descending, i = -1
            s[i + 1:] = s[i + 1:][::-1]

            # print('reverse s[i+1:] %s' % s)
            # print('**** s=%s' % s)
            return s

        num1 = num
        while k:
            num1 = next_perm(list(num1))
            k -= 1

        # print('k-th perm %s' % num1)

        def count_adj_swaps(num, num1):
            # 1. find num[i] != num1[j]
            i, j, ans = 0, 0, 0
            for i in range(n):
                j = i
                while j < n and num[i] != num1[j]:  # 1. 在nums1中找到一个和num[i]相同的char
                    j += 1
                while i < j:  # 相邻两个元素交换，直到把nums1[j]换到nums1[i]的位置，同时递减j，和结果计数
                    num1[j - 1], num1[j] = num1[j], num1[j - 1]
                    j -= 1
                    ans += 1
            return ans

        return count_adj_swaps(num, num1)


def main():
    sol = Solution()

    assert sol.getMinSwaps(num = "5489355142", k = 4) == 2, 'fails'

    assert sol.getMinSwaps(num = "11112", k = 4) == 4, 'fails'


if __name__ == '__main__':
   main()