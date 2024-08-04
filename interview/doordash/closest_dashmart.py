# Closest DashMart

# A DashMart is a warehouse run by DoorDash that houses items found in convenience stores,
# grocery stores, and restaurants. We have a city with open roads, blocked-off roads, and DashMarts.

# City planners want you to identify how far a location is from its closest DashMart.

# You can only travel over open roads (up, down, left, right).

# Locations are given in [row, col] format.

# Example 1
# [
#      0    1    2    3    4    5    6    7    8
#    ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'], # 0
#    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'], # 1
#    [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
#    [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
#    [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
#    [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']  # 5
# ]

# ' ' represents an open road that you can travel over in any direction (up, down, left, or right).
# 'X' represents an blocked road that you cannot travel through.
# 'D' represents a DashMart.

# list of pairs [row, col]
# locations = [
#    [200, 200], // out of bound -> -1
#    [1, 4],
#    [0, 3], // start from dashmart
#    [5, 8],
#    [1, 8],
#    [5, 5]
# ]

# answer = [-1, 2, 0, -1, 6, 9]


# Provided:
# - city: char[][]
# - locations: int[][2]

# Return:
# - answer: int[]
# Return a list of the distances from a given point to its closest DashMart.


# Follow up:
# There are now customers in the city! Each customer is represented by a 'C'. The city #planners want to know which DashMarts will service the most customers. Assume that #customers will always be served by their closest DashMarts. In the case of a tie, the #customer can use any of the closest DashMarts.
# If there are multiple DashMarts serving the highest number of customers, then return #all of them.
# [
#    # 0,   1,   2,   3,   4,   5,   6,   7,   8
#    ['C', ' ', 'D', 'C', 'D', 'C', 'X', ' ', 'C'], # 0
#    ['X', 'D', 'C', 'X', ' ', ' ', ' ', ' ', 'X']  # 1
# ]

# The DashMart at [0, 2] serves 3 customers at [[1, 2], [0, 0], [0, 3]].
# The DashMart at [0, 4] serves 3 customers at [[0, 3], [0, 5], [0, 8]].
# The DashMart at [1, 1] serves 2 customers at [[0, 0], [1, 2]]
# answer = [[0, 2], [0, 4]] # (in any order)


# [
#    # 0,   1,   2,   3,   4,   5,   6,   7,   8
#    ['C', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'C'], # 0
#    ['X', ' ', 'C', 'X', 'C', ' ', ' ', ' ', 'X'], # 1
#    [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '], # 2
#    [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '], # 3
#    ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'], # 4
#    ['D', 'X', ' ', 'C', 'C', ' ', ' ', 'X', 'C']  # 5
# ]

# The DashMart at [3, 3] serves 2 customers at [[5, 3], [5, 4]].
# The DashMart at [2, 3] serves 1 customer at [1, 2].
# The DashMart at [0, 3] serves 4 customers at [[1, 2], [0, 0], [1, 4], [0, 8]]
# answer = [[0, 3]]

from collections import deque
import math


def closest(city, locations):
    m, n = len(city), len(city[0])
    ans = []
    for x, y in locations:
        if x < 0 or x >= m or y < 0 or y >= n:
            ans.append(-1)
            continue
        q = deque([(x, y, 0)])
        shortest_dist = math.inf
        visited = set([(x, y)])
        while q:
            i, j, dist = q.popleft()
            if city[i][j] == 'D':
                shortest_dist = min(shortest_dist, dist)
                break
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for ni, nj in [(i + di, j + dj) for di, dj in dirs]:
                if 0 <= ni < m and 0 <= nj < n and city[ni][nj] != 'X' and (ni, nj) not in visited:
                    q.append((ni, nj, dist + 1))
                    visited.add((ni, nj))

        if not shortest_dist < math.inf:
            shortest_dist = -1
        ans.append(shortest_dist)

    return ans


def test_example_1():
    city = [
        #     0    1    2    3    4    5    6    7    8
        ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],  # 0
        ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],  # 1
        [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],  # 2
        [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],  # 3
        [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],  # 4
        [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']  # 5
    ]

    locations = [
        [200, 200],
        [1, 4],
        [0, 3],
        [5, 8],
        [1, 8],
        [5, 5]
    ]

    expected_answer = [-1, 2, 0, -1, 6, 9]
    result = closest(city, locations)
    print(result)
    assert result == expected_answer


def test_example_2():
    city = [
        ['D', 'X', 'X'],
        ['D', 'D', 'X']
    ]

    locations = [[0, 2], [1, 1], [1, 2]]

    expected_answer = [-1, 0, 1]
    result = closest(city, locations)
    print(result)
    assert result == expected_answer


def test_no_dashmarts():
    city = [
        # 0,   1,   2,   3,   4,   5,   6,   7,   8
        [' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' '],  # 0
        ['X', 'X', 'X', ' ', ' ', 'X', ' ', ' ', 'X'],  # 1
    ]
    locations = [[0, 3], [0, 5], [1, 8]]
    expected_answer = [-1, -1, -1]
    result = closest(city, locations)
    print(result)
    assert result == expected_answer


# test_example_1()
# test_example_2()
# test_no_dashmarts()


from collections import deque, defaultdict
import math


def customer_counts(city):
    m, n = len(city), len(city[0])
    counts = defaultdict(int)
    for x in range(m):
        for y in range(n):
            if city[x][y] != 'C':
                continue
            q = deque([(x, y, 0)])
            closest_dashmart = None
            visited = set([(x, y)])
            while q:
                i, j, dist = q.popleft()
                if city[i][j] == 'D':
                    closest_dashmart = (i, j)
                    break
                dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for ni, nj in [(i + di, j + dj) for di, dj in dirs]:
                    if 0 <= ni < m and 0 <= nj < n and city[ni][nj] != 'X' and (ni, nj) not in visited:
                        q.append((ni, nj, dist + 1))
                        visited.add((ni, nj))

            if closest_dashmart is not None:
                counts[closest_dashmart] += 1

    if counts:
        max_count = max(counts.values())
        return [list(key) for key, val in counts.items() if val == max_count]
    else:
        return []


def test_simple_example():
    city = [
        # 0,   1,   2,   3,   4,   5,   6,   7,   8
        ['C', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'C'],  # 0
        ['X', ' ', 'C', 'X', 'C', ' ', ' ', ' ', 'X'],  # 1
        [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],  # 2
        [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],  # 3
        ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],  # 4
        ['D', 'X', ' ', 'C', 'C', ' ', ' ', 'X', 'C']  # 5
    ]
    expected_answer = [[0, 3]]
    result = customer_counts(city)
    print(result)
    assert result == expected_answer


def test_fork_and_rejoin():
    """
    Since a customer can be use multiple DashMarts, we have to make sure
    that a single DashMart isn't being counted twice for the same customer
    if it's reachable from 5 separate paths of the same distance:
    DashMart at [1, 0] and the customer at [1, 2]
    """
    city = [
        # 0,   1,   2,   3,   4,   5,   6,   7,   8
        ['D', ' ', ' ', ' ', ' ', 'C', 'D', ' ', ' '],  # 0
        [' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', 'X'],  # 1
        [' ', ' ', 'C', ' ', ' ', ' ', ' ', 'X', 'X'],  # 2
    ]
    expected_answer = [[0, 6]]
    result = customer_counts(city)
    print(result)
    assert result == expected_answer


def test_no_dashmarts():
    city = [
        # 0,   1,   2,   3,   4,   5,   6,   7,   8
        [' ', ' ', ' ', ' ', ' ', 'C', 'C', ' ', ' '],  # 0
        ['C', 'X', 'C', ' ', ' ', 'C', ' ', ' ', 'X'],  # 1
    ]
    expected_answer = []
    result = customer_counts(city)
    print(result)
    assert result == expected_answer


def test_multiple_closest_dashmarts():
    city = [
        # 0,   1,   2,   3,   4,   5,   6,   7,   8
        ['C', ' ', 'D', 'C', 'D', 'C', 'X', ' ', 'C'],  # 0
        ['X', 'D', 'C', 'X', ' ', ' ', ' ', ' ', 'X']  # 1
    ]
    expected_answer = [[0, 2], [0, 4]]  # (in any order)
    result = customer_counts(city)
    print(result)
    assert len(result) == len(expected_answer)
    for dashmart_coordinate_list in expected_answer:
        assert (dashmart_coordinate_list in expected_answer)


test_simple_example()
test_no_dashmarts()
test_fork_and_rejoin()
test_multiple_closest_dashmarts()