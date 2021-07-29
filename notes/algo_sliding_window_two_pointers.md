# 滑动窗口 (sliding window) / 双指针 Two Pointers

https://leetcode.com/problems/sliding-window-maximum/

Given a array of integers (stream) nums, there's a sliding window of size k which is from from very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

双指针可以把O(n2)O(n2)变成O(n)O(n)，靠的就是单调性。
单调性含义：随i的增加，j一直延一个方向变化，就是单调性。比如，随i的增加，j也一直增加，这叫单调递增，如随i的增加，j一直减小，这叫单调递减，总之随i的增加，j一会增，一会减就没有单调性了。

## 滑动窗口适用问题：
* 0. 一般只适用于正数,如果有负数一般用 monotonic increasing/decreasing deque
* 1. 连续的元素，比如string，subarray， linkedlist
* 2. min, max, longest, shortest, keyword
* 3. 数据量维度10^4，N^2不可行，考虑滑动窗口

## 双指针类型
第一种 i 从0到n，j从0到i-1，随i走
第二种 i 从0到n，j从i到n-1，探索滑动窗口最大右边界

## 普通滑动窗口模板
    步骤：
        进：当前char 入map
        出：删除左端不符合的char
        算：计算更新substring长度

    1) two pointers, iterate right index, explore left, use hashmap (dict) to store counts of each char within the current window
       time O(N*K)
       space O(K)
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lastpos = collections.defaultdict(int) # left boundary of sliding window, for string with letters only, we can use array
        left = 0
        for i, c in enumerate(s):
            if c in lastpos:
                del lastpos[c] # 删除再加入，这样保证新加入的c在ordereddict lastpos里面是最后一个
                laspos[c] = i # 1 进： 当前遍历的i进入窗口
            else:
                laspos[c] = i # 1 进： 当前遍历的i进入窗口
                while len(lastpos) > k: # 1 出：当窗口不符合条件时left持续退出窗口
                    _, del_idx = lastpos.popitem(last=False) # poping first, i.e., remove left most char
                    left = del_idx + 1 # update window left boundary
            res = max(res, i-left+1)

        return res

    1) two pointers, iterate right index, explore left, use ordereddict to store last position of each char within the current window
       time O(N)
       space O(K)
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counts = OrderedDict() # last position of each char in current window
        left = 0
        for i, c in enumerate(s):
            counts[c] += 1 # 1 进： 当前遍历的i进入窗口
            while len(counts) > k: # 1 出：当窗口不符合条件时left持续退出窗口
                c = s[left]
                counts[c] -= 1
                if counts[c] == 0: del counts[c] # 如果该字符count减到0，从dict删除该key
                left += 1 # 出时需要向右移动左指针
            res = max(res, i-left+1)

        return res

## sliding window max/min using monotonic deque - positive number only
* sliding window max (deque) notes:
    1. sliding window max stores array index in the monotonic decreasing deque
    2. when new element pops larger older element from the end of deque, it is compared by value (nums[q[-1]]<nums[i])
    3. when old (front of queue) element goes out of focus gets kicked out, it is compared using index (q[0]+k<i)
    4. after we kicked out larger element from end of queue, we then add the new item
       q.append(nums[i])
    5. we pops out element from front of queue when it is too old (out of window size k) for next i (iteration increases i)

* sliding window max using deque steps

  1. maintain a monotonic decreasing deque (storing index instead of value) by poping out back elements smaller than nums[i]
  2. check if head element is out of date (in terms of sliding window)
  3. The current head element of the deque is the maximum of the sliding window

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()
        ans = []
        for i in range(n):
            # add item nums[i] (index) into dq, while maintaining monotonic decreasing deque (value decreasing)
            # i.e., if dq right end nums[dq[-1]] < nums[i], drop nums[dq[-1]]
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            # now either dq is empty, or nums[dq[-1]] >= nums[i]
            dq.append(i)
            # drop items that are out of window k (index)
            while dq and dq[0] <= i - k:
                dq.popleft()
            # now all items in dq are valid within i-k to i-1, dq[0] is the max
            if i >= k - 1:
                ans.append(nums[dq[0]])

* monotonic deque to find smallest nums[j] s.t. i<j and nums[j]>nums[i], i.e., smallest larger value to right
  1. sort A with index to find minmum larger number nums[j] to right of i s.t., i<j, and nums[j]>nums[i] and nums[j] is the smallest such value

    def oddEvenJumps(self, A):
        n = len(A)
         stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_min_higher[stack.pop()] = i
            stack.append(i)

## Sliding window with negative number
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/189039/Detailed-intuition-behind-Deque-solution
- because with negative number, the subarray sum is not monotonic increasing with length of subarray, so regular sliding window won't work
- however, we can calculate prefix sum, use monotonic increasing deque to store index of inreasing prefix sum, i.e., possible values of start pointer for valid window. and apply sliding window tech on the increasing prefix sum sequence
- why use increasing deque? - only these values can be possible valid subarray start, keep other values that cannot be valid subarray start would cause no monotonic thus cannot use sliding window tech
- why use prefixsum instead original array? - we cannot do add value as right pointer move right, and subtract value as left pointer move right, as the deque is a subsequence of possible start pointer, it is not continuous, therefore we use prefix sum, and can still calculate sliding window sum using presum[j]-presum[i]
- why deque? - it allows O(1) pop_left, append_right and pop_right.
    def shortestSubarray(self, A, K):
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N):
             B[i + 1] = B[i] + A[i]
        d = collections.deque()
        res = N + 1
        for i in xrange(N + 1):
              while d and B[i] - B[d[0]] >= K: res = min(res, i - d.popleft())
              while d and B[i] <= B[d[-1]]: d.pop()
              d.append(i)
        return res if res <= N else -1
