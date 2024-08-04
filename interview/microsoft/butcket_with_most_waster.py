"""
接雨水问题

https://leetcode.com/problems/container-with-most-water/

给定 $n$ 个非负整数 $a_1，a_2，…，a_n$，每个数代表坐标中的一个点 $(i, a_i)$ 。在坐标内画 $n$ 条垂直线，垂直线 $i$ 的两个端点分别为 $(i, a_i)$ 和 $(i, 0)$。找出其中的两条线，使得它们与 $x$ 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 $n$ 的值至少为 2。


示例1
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
 
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

接雨水问题解析
方法二：双指针法
两线段之间形成的区域总是会受到其中较短那条长度的限制。我们使用两个指针，一个放在开始，一个置于末尾。 在每一步中，我们会计算指针所指向的两条线段形成的区域面积，并将指向较短线段的指针向较长线段那端移动一步。如下：

接雨水问题解析
方法二：双指针法
两线段之间形成的区域总是会受到其中较短那条长度的限制。我们使用两个指针，一个放在开始，一个置于末尾。 在每一步中，我们会计算指针所指向的两条线段形成的区域面积，并将指向较短线段的指针向较长线段那端移动一步。如下：

public static int maxArea2(int[] height) {
 
    int max = 0;
    int current = 0;
    int left = 0;
    int right = height.length-1;
 
    while(left < right){
        current = (right - left) * Math.min(height[left],height[right]);
        max = Math.max(max,current);
 
        if(height[left] < height[right]){
            left ++ ;
        }else{
            right -- ;
        }
    }
 
    return max;
}

"""


from typing import List

class Solution:
    def rain_water(self, height: List[int]) -> int:
        pass

def main():
    sol = Solution()
    assert sol.rain_water(height = [0,1,0,2,1,0,1,3,2,1,2,1]) == 6, 'fails'

    assert sol.rain_water(height = [4,2,0,3,2,5]) == 9, 'fails'

if __name__ == '__main__':
   main()