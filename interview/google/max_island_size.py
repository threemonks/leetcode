"""

类似最大岛屿面积，但岛屿包围的水也算岛屿的面积

从边上出发，把所有的水（0）都标记成2
这样matrix里面剩下的只有1（地）和0（被1包围的水）
然后做dfs，dfs遇到1和0都可以计入面积。跳过2


"""