"""
[[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
[0 1 0 0 0]
get(3) => -1 [-1 -1 -1 -1 -1]
set(2) => 1  [2 2 -1 -1 -1]
get(1) => 2  [2 2 -1 -1 -1]
get(3) => -1 [2 2 -1 -1 -1]
get(2) => 2  [2 2 -1 -1 -1]

maybe store smallest index to right with value 1

"""


def answerQueries(queries, N):
    n = len(queries)
    values = [0 for _ in range(n)]
    ans = []
    for i in range(n):
        t, idx = queries[i]
        if t == 1:
            values[idx - 1] = 1
        elif t == 2:
            # get smallest index >= idx with value 1
            found = False
            for j in range(idx-1, n):
                if values[j] == 1:
                    ans.append(j+1)
                    found = True
            if not found:
                ans.append(-1)

    return ans

def main():

    assert answerQueries([[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]], 5 ) == [-1, 2, -1, 2], 'fails'

if __name__ == '__main__':
    main()
