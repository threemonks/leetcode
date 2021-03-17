"""
478. Generate Random Point in a Circle
Medium
"""
from math import sqrt
from random import random
from typing import List

from random import random

"""
Rejection Sampling

geneate random number between [0, 1], scale to [0, 2], then minus -1 to get to range [-1, 1]. So we now have uniform sampling within square -1<=x<=1 and -1<=y<=1, we then reject any points that has distance from (0, 0) larger than 1.

Finally scale to radius and move to center (x_center, y_center)

"""


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # generate a (x,y) pair within circle (0, 0) r=1
        x, y = random(), random()
        while sqrt((2 * x - 1) ** 2 + (2 * y - 1) ** 2) > 1:
            x, y = random(), random()

        # map to desired circle center and radius
        return [(2 * x - 1) * self.radius + self.x_center, (2 * y - 1) * self.radius + self.y_center]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()