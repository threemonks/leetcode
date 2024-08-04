"""
堆箱子问题

https://www.1point3acres.com/bbs/thread-772154-1-1.html

给你一堆n个箱子，箱子宽 $w_i$、深 $d_i$、高 $h_i$。箱子不能翻转，将箱子堆起来时，下面箱子的宽度、高度和深度必须大于上面的箱子。实现一种方法，搭出最高的一堆箱子。箱堆的高度为每个箱子高度的总和。

输入使用数组$[w_i, d_i, h_i]$表示每个箱子。

示例1:
输入：box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
输出：6
示例2:
输入：box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
输出：10

"""
from functools import lru_cache
from typing import List
"""
1、回溯算法
先想出暴力解法，即以每个箱子为最底下的箱子。然后在余下的箱子中寻找下一个箱子，下一个箱子自然是比前一个要小的，而后再寻找更小的。这就是一个 dfs 的过程。

选择一个箱子作为作为底之后，可以把问题转换为在约束条件下，求其余箱子能叠出的最大高度。可以把子问题的解（以每个箱子为底所能得到的最大高度）缓存下来，以加速计算。另外，可以在维度上进行升序排列，这样当前箱子后面的所有箱子都不可能处于该箱子之上。 所以操作如下：
    排序（升序）
    遍历，将各个箱子作为底
    在剩下的箱子中，以2步骤的箱子为底和约束条件下，寻找合适的箱子，递归重复2，直到所有箱子。计算高度和。
    在高度和中取最大值。

class Solution {
public:
    int pileBox(vector<vector<int>>& box) {
        sort(box.begin(), box.end(), [](auto& a, auto& b){
            return a[0] < b[0];
        });
        vector<int> cache(box.size(), -1);
        int max_height = 0;
        for(int i = 0; i < box.size(); i++){
            max_height = max(max_height, dfs(box, i, cache));
        }
        return max_height;
    }
 
    int dfs(vector<vector<int>>& box, int bottom_box_i, vector<int>& cache){
        if(cache[bottom_box_i] != -1){
            return cache[bottom_box_i];
        }
        int ret = 0;
        vector<int> &bottom_box = box[bottom_box_i];
        for(int i = 0; i < bottom_box_i; i++){
            if(small(box[i], bottom_box)){
                ret = max(ret, dfs(box, i, cache));
            }
        }
        ret = ret + bottom_box[2];
        cache[bottom_box_i] = ret;
        return ret;
    }
     
    bool small(const vector<int> &box1, const vector<int> &box2){
        for(int i = 0;i<box1.size();i++){
            if(box1[i] >= box2[i]){
                return false;
            }
        }
        return true;
    }
};
 
"""
class Solution0:
    def pile_box(self, nums: List[List[int]]) -> int:
        pass


"""

2、动态规划

本题类似于俄罗斯套娃，都属于最长递增子串问题。也就是在一维的数组中找到该数列的递增次序，如下图所示：




最终紫色的序列1,2,3就是最后的最长递增子串。放到这道题来讲，我们先要将三维的排序，对于第一维相同的，就采用第二维的子串递增，如果第二维也相同，那么就找第三维的子串递增序列。下图是一个二维的示例：




所以对于该题的算法操作如下：
先将数组按照任何一条边降序重排，目的是为了降低里层循环次数。
使用dp一维数组记录以序号$i$箱子为顶时的最大高度。
计算每个箱子$i$时，在约束条件下，找到所有箱子$k$（$i$可以放在$k$的上面），并计算以k为顶最大高度与$i$的高度之和，取最大值。
所有箱子都操作完后，取dp数组元素的最大值

class Solution {
public:
    int pileBox(vector<vector<int>>& box) {
        sort(box.begin(), box.end(), [](auto& a, auto& b){
            return a[0] < b[0];
        });
        vector<int> dp(box.size(), 0);
        dp[0] = box[0][2];
        int ret = dp[0];
        for(int i = 1; i < box.size(); i++){
            int max_height = 0;
            for(int j = 0; j < i; j++){
                if(small(box[j], box[i])){
                    max_height = max(max_height, dp[j]);
                }
            }
            dp[i] = max_height + box[i][2];
            ret = max(ret, dp[i]);
        }
        return ret;
    }
     
    bool small(const vector<int> &box1, const vector<int> &box2){
        for(int i = 0;i<box1.size();i++){
            if(box1[i] >= box2[i]){
                return false;
            }
        }
        return true;
    }
};

time O(N^2)
"""

class Solution1:
    def pile_box(self, boxes: List[List[int]]) -> int:
        boxes = sorted(boxes)
        print(boxes)
        n = len(boxes)
        dp = [0 for _ in range(n)] # max height with box[i] as top of pile
        dp[0] = boxes[0][2] # smallest box's height, as top

        ans = dp[0]
        def small(box1, box2):
            """
            is box1 strictly smaller than box2, in all three dimensions
            """
            return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

        for i in range(1, n):
            max_height = 0
            for j in range(i):
                if small(boxes[j], boxes[i]):
                    max_height = max(max_height, dp[j])
            dp[i] = max_height + boxes[i][2]
            ans = max(ans, dp[i])
            print('i=%s max_height=%s dp=%s ans=%s' % (i, max_height, dp, ans))

        print(ans)
        return ans

"""
recursive dfs to find max height with a given box as base, what are max height for all other boxes (restricted by this box's size)

time O(N^2)
"""
class Solution:
    def pile_box(self, boxes: List[List[int]]) -> int:
        boxes = sorted(boxes)
        print(boxes)
        n = len(boxes)
        memo = {}

        def small(box1, box2):
            """
            is box1 strictly smaller than box2, in all three dimensions
            """
            return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

        def dfs(box):
            # max height with this box as base
            if tuple(box) in memo:
                return memo[tuple(box)]
            max_height = 0
            for i in range(n):
                if small(boxes[i], box):
                    max_height = max(max_height, dfs(boxes[i]))

            memo[tuple(box)] = box[2]+max_height
            return memo[tuple(box)]

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(boxes[i]))

        print(ans)
        return ans

def main():
    sol = Solution()
    assert sol.pile_box(boxes=[[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 6, 'fails'

    assert sol.pile_box(boxes=[[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]) == 10, 'fails'

if __name__ == '__main__':
   main()