"""
逃脱阻碍

https://leetcode.com/problems/escape-the-ghosts/

你在进行一个简化版的吃豆人游戏。你从 [0, 0] 点开始出发，你的目的地是 $target = [x_target, y_target]$ 。地图上有一些阻碍者，以数组 ghosts 给出，第 $i$ 个阻碍者从 $ghosts = [x_i, y_i]$ 出发。所有输入均为整数坐标 。
每一回合，你和阻碍者们可以同时向东，西，南，北四个方向移动，每次可以移动到距离原位置 1 个单位 的新位置。当然，也可以选择不动 。所有动作同时发生。
如果你可以在任何阻碍者抓住你之前到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者同时到达了一个位置（包括目的地）都不算是逃脱成功。
只有在你有可能成功逃脱时，输出 true ；否则，输出 false 。

示例 1:
输入：
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
输出：true
解释：你可以直接一步到达目的地(0,1)，在(1, 0)或者(0, 3)位置的阻碍者都不可能抓住你。

示例 2:
输入：
ghosts = [[1, 0]]
target = [2, 0]
输出：false
解释：你需要走到位于(2, 0)的目的地，但是在(1, 0)的阻碍者位于你和目的地之间。

示例 3:
输入：
ghosts = [[2, 0]]
target = [1, 0]
输出：false
解释：阻碍者可以和你同时达到目的地。

示例 4：
输入：
ghosts = [[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]],
target = [7,7]
输出：false

示例 5：
输入：
ghosts = [[-1,0],[0,1],[-1,0],[0,1],[-1,0]],
target = [0,0]
输出：true


对于这道题，可能有部分人会先建图，然后广搜、深搜啥的，其实这道题就是一个数学问题。阻碍者最好的抓住你的办法就是在终点等你。数学证明如下： 如果鬼魂要在中间拦截 AC上必须有一点D 使得AD = DB ，通过三角不等式 AC = AD + DC = DB + DC >= BC 。 如果鬼魂可以拦截到，那么鬼魂最好的做法就是在终点等着而不是去中间拦截。上面选择的是最短路径，乱走的话，相信鬼魂会笑的更开心！！！

/** A表示起点 ，B表示鬼魂的位置 ，目的地为C 。
*
*          C
*         /  \
*        /    \
*       /      \
*      /        \
*     /   \D     \
*    /      \     \
*   /         \    \
*  /            \   \
* A               \
*                     B
*
* */
而你到达target的最短距离就是abs(target[0]) + abs(target[1])，每个阻碍者到达终点的最短距离就是 abs(ghost[0]-target[0])+abs(ghost[1]-target[1])，因此我们只要比较两者的大小即可。

class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        int myMindistance = abs(target[0]) + abs(target[1]);//我到达终点的最短距离
        for (auto &ghost : ghosts){//判断是否有ghost比我先到达终点
            if (myMindistance >= abs(ghost[0]-target[0])+abs(ghost[1]-target[1])){
                return false;
            }
        }
        return true;
    }
};
复杂度分析

时间复杂度：$O(\text{ghosts}.\text{length})$
空间复杂度：$O(1)$
"""

class Solution:
    def valid_anagram(self, s1: str, s2: str) -> bool :
        return sorted(s1) == sorted(s2)

def main():
    sol = Solution()
    assert sol.valid_anagram('abc', 'bca') == True, 'fails'

if __name__ == '__main__':
   main()