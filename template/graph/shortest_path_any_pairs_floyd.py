"""
基于动态规划
复杂度 O(n^3)
求出任意两点最短路径
通过每一点松弛所有其他路径
递推式map[ i ][ j ] = min ( map[ i ][ j ], map[ i ][ k ] + map[ k ][ j ] )
关键代码

"""
import math


def floyd(graph, n):
    # 初始化：
    dist = [[math.inf for _ in range(n)] for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
