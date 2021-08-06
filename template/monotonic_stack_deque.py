"""
https://www.programmersought.com/article/48444590138/
Monotonic Decreasing Stack
"""
from collections import deque


def mono_inc_stack(nums):
    n = len(nums)
    ans = 0
    st = []
    for i in range(n):
        while st and nums[st[-1]] > nums[i]:
            st.pop()
            # update result
            ans = max(ans, nums[st[-1]])
        st.append(i)

    return ans

"""
Monotonic Decreasing Stack
"""

def mono_dec_stack(nums):
    n = len(nums)
    ans = 0
    st = []
    for i in range(n):
        while st and nums[st[-1]] < nums[i]:
            st.pop()
            # update result
            ans = max(ans, nums[st[-1]])
        st.append(i)

    return ans

"""
Monotonic Increasing Deque
Note: this does not use the unique property of deque, which is popleft, so deque is helpful if we need to do something to left end of stack, and do popleft
"""
def mono_inc_deque(nums):
    n = len(nums)
    dq = deque()
    ans = 0
    for i in range(n):
        while dq and nums[dq[-1]] > nums[i]:
            dq.pop()
            # update result
            ans = max(ans, nums[dq[-1]])
        dq.append(i)
    return ans

"""
Monotonic Decreasing Deque
"""
def mono_dec_deque(nums):
    n = len(nums)
    dq = deque()
    ans = 0
    for i in range(n):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            # update result
            ans = max(ans, nums[dq[-1]])
        dq.append(i)
    return ans