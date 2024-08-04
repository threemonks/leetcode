## 二分的使用条件和时间复杂度

* 必须是单调递增或者递减数组
  * 注意这里是单调递增或者递减,而不是全部递增或者递减，这点很重要。如果是完全乱序的数组，那么二分算法就会完全失效。二分的本质就是借助于单调性然后比较中间节点的值来达到缩小范围去查询元素的目的。如果是乱序的,那么就无法比对中间值来达到缩减区间的目的
  * 二分法所需的单调性就是i增加时需要的数值严格变大
  * 双指针（滑动窗口）所需要的单调性是当i增加时对应的j也增加

* 必须是线性结构

    对于像图二叉树等结构，二分是不合适的，因为没办法去用二分，这是由结构决定的

## 二分的时间复杂度
   二分查找的时间复杂度是o(logn)，关于二分的时间复杂度是怎么计算出来的呢？假如数组的长度是n，每次进行二分查找的时候是n/2，下次是n/4，再一次是n/8。在最坏的情况下，每次都找不到目标值，那么就有可以设查找的次数为T，（n/2）^T=1；则T=logn,底数是2，时间复杂度为O（logn）

##  How do we come to binary search
*) minimize/maximize problems can also be solved with binary search as long as the predicate function is monotonic. When the problem is asking to maximize/minimize something, you may think of using binary search or dp. If the predicate function is monotonic, i.e., if we can split with penalty X, we can also split it with penalty X+1, X+2, then we can use binary search.

*) One would first try to directly calculate the answer (brutal force). Usually if it works, it is a dp. But the range here is 10^9, even with dp, time complexity would be number of recursive calls of 10^5, that results in TLE. So we try  binary search.

*) If the problem has a brutal force with pattern false,false....true,true...true or the contrary, i.e., all False until some value, then all True, or all True and then all False, (monotonic), then one can use binary search.

## 不同二分模板

如果循环内部涉及mid和mid + 1做比较，那就选左闭右闭这个模板，因为我要保证mid + 1依然在搜索区间内。如果用了左闭右开，mid + 1的值有可能越界（当left + 1 == right, left == 算出来的mid的时候）。
如果循环内部只涉及mid和两端做比较，那就简单粗暴左闭右开。

## bisect module
bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.

An alternative question is when are they equivalent? By answering this, the answer to your question becomes clear.

They are equivalent when the the element to be inserted is not present in the list. Hence, they are not equivalent when the element to be inserted is in the list.

## Fundamentals of Binary Search
https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101
https://daimajiaoliu.com/daima/6cc85e7a84a2803
https://daimajiaoliu.com/daima/487220eaf900404

### Choice of lo and hi, aka the boundary
Normally, we set the initial boundary to the number of elements in the array

let lo = 0, hi = nums.length - 1;
But this is not always the case.
We need to remember: the boundary is the range of elements we will be searching from.

e.g., if we are search left or right boundary of a given target value, i.e., find first value > target, or last value < target, then we need to use 左闭右开 [0, n)
因为要搜索左右侧边界，所以索引最大位置必须大于数组长度，搜索的区间为[left, right)

### choice of mid
```
let mid = lo + Math.floor((hi - lo) / 2); // left/lower mid
let mid = lo + Math.floor((hi - lo + 1) / 2); // right/upper mid
````

### How do we shrink boundary
I always try to keep the logic as simple as possible, that is a single pair of if...else. But what kind of logic are we using here? My rule of thumb is **always use a logic that you can exclude mid**.
Let's see an example:

```
if (target < nums[mid]) {
	hi = mid - 1
} else {
	lo = mid;
}
```
Here, if the target is less than mid, there's no way mid will be our answer, and we can exclude it very confidently using hi = mid - 1. Otherwise, mid still has the potential to be the target, thus we include it in the boundary lo = mid.
On the other hand, we can rewrite the logic as:

```
if (target > nums[mid]) {
	lo = mid + 1; // mid is excluded
} else {
	hi = mid; // mid is included
}
```

### while loop
To keep the logic simple, I always use

while(lo < hi) { ... }
Why? Because this way, the only condition the loop exits is lo == hi. I know they will be pointing to the same element, and I know that element always exists.

### Avoid infinity loop
Remember I said a bad choice of left or right mid will lead to an infinity loop? Let's tackle this down.
Example:

let mid = lo + ((hi - lo) / 2); // Bad! We should use right/upper mid!

```
if (target < nums[mid]) {
	hi = mid - 1
} else {
	lo = mid;
}
```
Now, imagine when there are only 2 elements left in the boundary. If the logic fell into the else statement, since we are using the left/lower mid, it's simply not doing anything. It just keeps shrinking itself to itself, and the program got stuck.
We have to keep in mind that, the choice of mid and our shrinking logic has to work together in a way that every time, at least 1 element is excluded.

let mid = lo + ((hi - lo + 1) / 2); // Bad! We should use left/lower mid!

```
if (target > nums[mid]) {
	lo = mid + 1; // mid is excluded
} else {
	hi = mid; // mid is included
}
```
So when your binary search is stuck, think of the situation when there are only 2 elements left. Did the boundary shrink correctly?

### My rule of thumb when it comes to binary search:
* Include ALL possible answers when initialize lo & hi
* Don't overflow the mid calculation
* Shrink boundary using a logic that will exclude mid
* Avoid infinity loop by picking the correct mid and shrinking logic
* Always think of the case when there are 2 elements left

## Mechanical way to implement bug free binary search
- The most important edge case is left=0 and right = 1
- trick #1: for loop condition: to exit when left == right, the loop condition is “while left < right”, not “while left <= right”.
- trick #2: for mid type: **right_mid needs to go with right = mid – 1 and left_mid needs to go left = mid + 1**
  - **left_mid: (left+right)>>1 or (left+right)//2**
  - **right_mid: (left+right+1)>>1 or (left+right+1)//2**
- trick #3: just having one side to exclude mid: Either left = mid + 1 or right = mid - 1, not both
- trick #4: for the mid-inclusive moving boundary: which boundary to be the mid-exclusive boundary? It is the opposite of the boundary which will move when one occurrence of the target is met at a given middle point. Let’s call it mid-inclusive moving boundary.
- In summary, in binary search problems, we can define left and right as inclusive boundaries and use “while left < right” as the loop condition. Then we need to consider which side of the boundary to move when one incidence of target is met, which will determine the mid-inclusive boundary and subsequently the mid-exclusive boundary and mid type using trick #4, #3, #2 above.

## 二分查找和二分查找左右侧边界
https://daimajiaoliu.com/daima/487220eaf900404
* 第一个，最基本的二分查找算法：
- 因为我们初始化 right = nums.length - 1, 所以决定了我们的「搜索区间」是 `[left, right]`, 所以决定了 while (left <= right), 同时也决定了 left = mid+1 和 right = mid-1
- 因为我们只需找到一个 target 的索引即可， 所以当 `nums[mid] == target` 时可以立即返回

* 第二个，寻找左侧边界的二分查找：
- 因为我们初始化 right = nums.length， 所以决定了我们的「搜索区间」是 [left, right)， 所以决定了 while (left < right)， 同时也决定了 left = mid+1 和 right = mid
- 因为我们需找到 target 的最左侧索引， 所以当 `nums[mid] == target` 时不要立即返回， 而要继续缩减右侧边界以锁定左侧边界

* 第三个，寻找右侧边界的二分查找：
- 因为我们初始化 right = nums.length，所以决定了我们的「搜索区间」是 [left, right)， 所以决定了 while (left < right)， 同时也决定了 left = mid+1 和 right = mid
- 因为我们需找到 target 的最右侧索引， 所以当 `nums[mid] == target` 时不要立即返回， 而要收紧左侧边界以锁定右侧边界
- 又因为收紧左侧边界时必须 left = mid + 1，所以最后无论返回 left 还是 right，必须减一

### References
- https://reprog.wordpress.com/2010/04/25/writing-correct-code-part-1-invariants-binary-search-part-4a/
- https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101
- https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1121605/A-mechanical-way-to-implement-bug-free-binary-search-algorithms-python3
- https://www.topcoder.com/thrive/articles/Binary%20Search
- https://inky-hovercraft-849.notion.site/Binary-Search-45031b3e5bce497ca4f0913af31d70c3#4256b911d1ba4eae8e432cd3c439add4
